import os

from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    temperature=0, model="gpt-4o-mini", api_key=os.environ.get("OPENAI_API_KEY")
)
