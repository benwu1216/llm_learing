import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# Load environment variables from .env file
load_dotenv()
# Initialize the OpenAI chat model
llm = ChatOpenAI(model = "gpt-4o-mini")
# Test environment variable
response = llm.invoke("What is the capital of France?")
print(response.content)