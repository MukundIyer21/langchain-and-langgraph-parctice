from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_groq import ChatGroq
from langchain_classic.schema import AIMessage, HumanMessage
from langchain.agents import create_agent

import os
import streamlit as st

st.set_page_config(page_title="SQL Agent for Students", layout="centered")
st.title("SQL Agent for Students")



os.environ["GROQ_API_KEY"] =os.getenv("GROQ_API_KEY")



model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_tokens=150,
    max_retries=2,
)
db = SQLDatabase.from_uri("sqlite:///school.db")

toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()

system_prompt = """
You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run,
then look at the results of the query and return the answer. Unless the user
specifies a specific number of examples they wish to obtain, always limit your
query to at most {top_k} results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

You MUST double check your query before executing it. If you get an error while
executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
database.

To start you should ALWAYS look at the tables in the database to see what you
can query. Do NOT skip this step.

Then you should query the schema of the most relevant tables.
""".format(
    dialect=db.dialect,
    top_k=5,
)

agent_executor = create_agent(
    model,
    tools,
)

question = st.text_input("Enter your query:")

if question:
    st.markdown("---")
    st.subheader("🤖 Agent Response")
    
    with st.spinner("Thinking..."):
        try:
            for event in agent_executor.stream(
                {"messages": [("user", question)]},
                stream_mode="values"
            ):
                last_message = event["messages"][-1]
                if hasattr(last_message, 'content') and last_message.content:
                    if hasattr(last_message, 'type'):
                        if last_message.type == "human":
                            st.write(f"**You:** {last_message.content}")
                        elif last_message.type == "ai":
                            st.write(f"**Assistant:** {last_message.content}")
                        elif last_message.type == "tool":
                            with st.expander("🔧 Tool Execution"):
                                st.code(last_message.content)
                    else:
                        st.write(last_message.content)
            
        except Exception as e:
            st.error(f"Error executing agent: {str(e)}")





