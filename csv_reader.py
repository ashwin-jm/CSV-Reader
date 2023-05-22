import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import altair

openai_api_key = "your openai api key"

st.set_page_config(page_title="CSV Reader")
st.header("CSV Reader")
user_csv = st.file_uploader("Upload your CSV file", type="csv")
if user_csv is not None:
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
    agent = create_csv_agent(llm, user_csv, verbose=True)

    user_question = st.text_input("Enter your question")
    if user_question is not None and user_question != "":
        with st.spinner(text="In progress"):
            st.write(agent.run(user_question))
