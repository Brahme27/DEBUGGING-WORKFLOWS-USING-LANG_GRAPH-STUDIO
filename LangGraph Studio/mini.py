# agentDebugging.py

from typing import Annotated
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Setup API keys from .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")  # Important for LangSmith or LangGraph debugging

# Define shared state structure
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Base LLM model
model = ChatOpenAI(temperature=0)

# Default graph without tools
def simple_graph():
    graph = StateGraph(State)

    def call_model(state: State):
        return {"messages": [model.invoke(state["messages"])]}

    graph.add_node("agent", call_model)
    graph.add_edge(START, "agent")
    graph.add_edge("agent", END)

    return graph.compile()

# Graph with tools
def complicated_graph():
    @tool
    def add(a: float, b: float) -> float:
        """Adds two numbers"""
        return a + b

    model_with_tools = model.bind_tools([add])
    tool_node = ToolNode([add])

    def call_model(state: State):
        return {"messages": [model_with_tools.invoke(state["messages"])]}

    def should_continue(state: State) -> str:
        if state["messages"][-1].tool_calls:
            return "tools"
        else:
            return END

    graph = StateGraph(State)
    graph.add_node("agent", call_model)
    graph.add_node("tools", tool_node)

    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", should_continue)
    graph.add_edge("tools", "agent")

    return graph.compile()

# Choose the agent for debugging
# You can export either of the agents below

# agent = make_default_graph()
agent = complicated_graph()
