from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import openai
import tabulate

openai_api_key = "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"
user_csv = "C:/Users/Dell/PycharmProjects/NLQ/data.csv"

llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
agent = create_csv_agent(llm, user_csv, verbose=True)
response = agent.run("How many jobs are there in New York?")
print(response)


