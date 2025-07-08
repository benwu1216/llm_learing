import os
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# TypedDict：用于定义状态字典的类型，包含文本、分类、实体和摘要等字段，能够对键值类型进行严格检查
class State(TypedDict):  
	text: str             # 存储原始输入文本    
	classification: str   # 存储分类结果（例如类别）    
	entities: List[str]   # 存储提取出的实体列表（例如命名实体）    
	summary: str          # 存储文本的简洁摘要

llm = ChatOpenAI(model = 'gpt-4o-mini', temperature = 0)

def classification_node(state: State) -> State:
	"""   
	将文本分类为预定义的类别之一。   
	参数:    
		 state (State): 当前状态字典，包含待分类的文本   
	返回:  
			 dict: 返回包含 "classification" 键的字典，其值为分类结果   
	类别:  
			 - News: 新闻报道类       
			 - Blog: 个人或非正式写作       
			 - Research: 学术或科研内容      
			 - Other: 不属于以上类别的其它内容
	"""
	# 定义 prompt 模板，指示模型对给定文本进行分类   
	prompt = PromptTemplate(input_variables=["text"], template="Classify the following text into one of the categories: News, Blog, Research, Other. Text: {text}") 
	
	# 根据当前 state 中的文本格式化 prompt  
	message = HumanMessage(content=prompt.format(text=state["text"])) 
	# 调用语言模型对文本进行分类  
	classification = llm.invoke([message]).content.strip()   
	print("Do Classification.")
	# 返回包含分类结果的字典  
	return {"classification": classification}


def entity_extraction_node(state: State) -> State: 
	# 用于从文本中识别并提取命名实体（按人名、组织、位置分类）  
	# 创建实体提取 prompt 模板，指定需要查找的实体和格式（逗号分隔） 
	prompt = PromptTemplate( 
		input_variables=["text"],      
		template="Extract all the entities (Person, Organization, Location) from the following text. Text: {text}" 
	) 
	# 根据 state 中的文本格式化 prompt 并包装为 HumanMessage  
	message = HumanMessage(content=prompt.format(text=state["text"]))  
	# 发送给语言模型，获取响应，清除空白后按逗号分隔拆分为列表  
	entities = llm.invoke([message]).content.strip().split(", ") 
	print("Extract Entities.")
	# 返回包含实体列表的字典，将与 agent state 合并  
	return {"entities": entities}

def summarize_node(state: State) -> State:  
	# 创建摘要 prompt 模板，指示模型用一句话对文本进行总结    
	summarization_prompt = PromptTemplate.from_template(   
		"""Summarize the following text in one short sentence.       
		Text: {text}        
		Summary:"""   
	)   
	# 利用 "|" 运算符将 prompt 模板和语言模型连接起来形成一个 chain   
	# 运算符重载允许将 prompt 和模型组合成一个处理链
	# 这里的 chain 将 prompt 和模型结合起来，形成一个处理流程 
	chain = summarization_prompt | llm    
	# 执行 chain，将文本传递给模型进行摘要    
	response = chain.invoke({"text": state["text"]}) 
	print(f"Generated Summary\n")   
	# 返回包含摘要的字典，将合并进 agent state   
	return {"summary": response.content}

workflow = StateGraph(State)
# 向图中添加各个节点
workflow.add_node("classification_node", classification_node)
workflow.add_node("entity_extraction", entity_extraction_node)
workflow.add_node("summarization", summarize_node)
# 设置图的入口节点
workflow.set_entry_point("classification_node")# 定义图中各节点之间的边关系
workflow.add_edge("classification_node", "entity_extraction")
workflow.add_edge("entity_extraction", "summarization")
workflow.add_edge("summarization", END)
# 编译图
agent = workflow.compile()

sample_text = """
An agent in LangChain is an intelligent decision-making system that leverages a language model to reason 
about and execute actions using external tools. Unlike static chains, which follow a fixed sequence of steps, 
agents dynamically determine the next step based on the current context and available tools. Powered by prompt 
engineering and output parsing, LangChain agents can analyze instructions, invoke relevant tools such as search 
engines, calculators, or APIs, and iteratively refine their responses. This makes them highly adaptable for tasks 
like multi-step reasoning, tool-augmented question answering, and interactive dialogue systems.
"""

# 构造包含样本文本的初始 state
state_input = {"text": sample_text}
# 运行 agent 的全流程
result = agent.invoke(state_input)

# 输出各个部分的结果：
# 分类结果（News、Blog、Research 或 Other）
print("Classification:", result["classification"])

# 提取出的实体（人名、组织、地点等）
print("\nEntities:")
for entity in result["entities"]:
	print(entity)

# 生成的文本摘要
print("\nSummary:", result["summary"])



