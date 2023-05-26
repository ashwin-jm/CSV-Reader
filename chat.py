import streamlit as st
from streamlit_chat import message
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

openai_api_key = "your api key"

st.set_page_config(page_title="CSV Reader")

with st.sidebar:
    st.title("Datahut")
    st.markdown("""
    ## About
    This is a chatbot developed by Datahut to chat with your csv file and extract information from it.
    """)


def get_text():
    input_text = st.text_input("Enter your question")
    return input_text


def get_response(query):
    with st.spinner(text="In progress"):
        response = agent.run(query)
    return response

st.header("CSV Reader ")
user_csv = st.file_uploader("Upload your CSV file", type="csv")
if user_csv is not None:
    user_input = get_text()
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
    agent = create_csv_agent(llm, user_csv, verbose=True)
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Yes, you can!"]
    if 'past' not in st.session_state:
        st.session_state['past'] = ["Can I ask anything about my csv file?"]
    if user_input:
        st.session_state.past.append(user_input)
        response = get_response(user_input)
        st.session_state.generated.append(response)
    if len(st.session_state['generated']) != 1:
        for i in range(1,len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i)+'_user')
            message(st.session_state['generated'][i], key=str(i))
