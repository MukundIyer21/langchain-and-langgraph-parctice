# LangChain and LangGraph Practice

This repository contains a collection of Jupyter notebooks and Python scripts that explore different use cases and workflows using **LangChain** and **LangGraph** — frameworks for building LLM-powered applications, retrieval-augmented generation (RAG), and agent-based systems.

---

## Repository Structure and File Descriptions

| File | Description |
|------|--------------|
| **Langgraph_Adaptive_RAG.ipynb** | Demonstrates adaptive Retrieval-Augmented Generation (RAG) using LangGraph. Shows how to retrieve and adapt context dynamically. |
| **SQL_LANGCHAIN.py** | Python script that uses LangChain to query a SQL database using an agent workflow. |
| **crew_graphdb.ipynb** | Focuses on graph database operations (in a “crew” database context) and integration with LangGraph. |
| **graph_with_tools.ipynb** | Demonstrates how to build LangGraph workflows that integrate tool-calling capabilities for dynamic execution. |
| **hybrid_search.ipynb** | Implements hybrid search combining vector and keyword-based search using LangChain or related libraries. |
| **langgraph_human_loop.ipynb** | Showcases a human-in-the-loop workflow built with LangGraph, allowing user oversight and corrections. |
| **langgraph_orchestrator_worker.ipynb** | Implements the orchestrator–worker pattern using LangGraph to divide and coordinate subtasks between agents. |
| **langgraph_parallel.ipynb** | Demonstrates parallel graph execution where multiple graph nodes or paths run concurrently. |
| **langgraph_prompt_chaining.ipynb** | Explores prompt chaining—sequentially connecting prompts to form a multi-step reasoning pipeline. |
| **langgraph_router.ipynb** | Shows routing logic in LangGraph, deciding which node or branch to follow based on input data or context. |
| **text_summarization.ipynb** | Implements text summarization workflows using LangChain and LangGraph components. |
| **requirements.txt** | Lists all Python dependencies required to run the notebooks and scripts. |
| **school.db** | SQLite database used by the SQL and graph notebooks for query and data management demonstrations. |
| **testDB.py** | Python script that connects to and queries the `school.db` database for testing purposes. |
| **README.md** | This documentation file describing the contents of the repository. |

---
   git clone https://github.com/MukundIyer21/langchain-and-langgraph-parctice.git
   cd langchain-and-langgraph-parctice
