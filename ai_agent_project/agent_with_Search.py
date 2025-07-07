import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

load_dotenv()

# 定义模型
llm = ChatOpenAI(model = "gpt-4o-mini")

# 定义记忆存储
memory = MemorySaver()

# 定义搜索工具
search_tool = TavilySearchResults(max_results = 2)
tools = [search_tool]

# 创建代理（使用模型、工具、记忆存储)
agent_executor = create_react_agent(llm, tools, checkpointer=memory)

# 使用代理进行聊天
config = {"configurable": {"thread_id": "abc123"}}

while True:
    query = input("请输入问题:")
    for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content=query)]}, config
    ):
        print(chunk)
        print("----")
    print('\n')

