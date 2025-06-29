# LangGraph Studio 
is a **visual debugging and observability tool** for workflows built using **LangGraph**, which is a framework for creating **stateful, multi-agent AI workflows**. It lets you understand what your graph (workflow) is doing at each step — very useful when building complex agent systems or chaining multiple LLM calls and tools.

## To run the code use this command
langgraph dev 

### **What You Can Do in LangGraph Studio**

When you **execute a workflow using LangGraph**, here's what **LangGraph Studio** enables:

### **1. Visualize Workflow Execution (Graph View)**

* See the **entire graph structure**: nodes, edges, flow.
* Understand how **states move from one node to another**.
* See **which node is being executed currently**, and which nodes were skipped or completed.

**Example:**
If your graph has steps like: `Input ➝ Search Tool ➝ LLM ➝ Summarizer ➝ Output`,
you’ll see exactly which node the state is in.

### **2. Step-by-Step Debugging (Node Execution Details)**

* View **inputs and outputs** for each node.
* Check the **state before and after** each step.
* Useful for debugging **why a node fails** or returns unexpected results.

### **3. Inspect State Transitions**

* View how the **state dictionary (e.g., `messages`, `tools_used`, etc.) evolves**.
* Useful when using complex types like `TypedDict`, `Annotated`, etc.
* Helps ensure data is flowing and transforming correctly.

###  **4. Replay & Iterate Faster**

* Re-run the same input and **see the differences**.
* Try new versions of your workflow and **compare results**.
* Helps in **fine-tuning your prompts, tools, or logic**.

### **5. Error Tracking & Logs**

* See **errors with stack traces** directly in the node where they occurred.
* Helps you quickly identify and fix bugs in tools, reducers, or LLM logic.

### **6. Collaboration & Sharing (Upcoming/Planned)**

* In future or enterprise versions, you may:

  * Share workflow runs with teammates.
  * Annotate parts of the graph.
  * Maintain execution history.

### Real Use Case Example:

Suppose you build a **research assistant agent** with the following workflow:

* `User Input ➝ Tool Selector ➝ Web Search ➝ LLM Summary ➝ Final Output`

LangGraph Studio helps you:

* See which tools were selected.
* Track how the message passed through.
* Debug why the LLM gave a weak response.
* Inspect if web search results were properly fed into the summarizer.
  
### Summary:

LangGraph Studio is your **control room** when building agentic workflows. It turns a black-box LLM pipeline into a **clear, visual, debuggable system**.

If you’ve ever struggled to understand **why a LangChain agent behaves oddly**, LangGraph Studio gives you **X-ray vision into your agents and tools**.