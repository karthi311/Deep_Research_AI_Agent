import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

# Load API keys
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set API keys (required for LangChain and Tavily)
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

llm = ChatGroq(
    temperature=0.2,
    model_name="llama3-8b-8192"  # ✅ Supported by Groq
)

# Define the Tavily tool
search_tool = TavilySearchResults(max_results=3)

# chat history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True,input_key = "input")


prompt = PromptTemplate.from_template("""
You are an AI assistant helping with research questions.

Here is the conversation so far:
{chat_history}

Current question:
{input}

Based on the following research context, draft a clear and concise answer(If urls or links present also include that too):

--Ensure the answer is informative and well-organized.

""")

chat_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)

def research_agent(input_query: str) -> str:
    print("[Research Agent] Gathering information for:", input_query)
    try:
        results = search_tool.run(input_query)
        
        if isinstance(results, str):
            return f"Search results for '{input_query}':\n{results}"
        
        if isinstance(results, list):
            extracted_data = []
            for i, r in enumerate(results):
                if isinstance(r, dict):
                    content = r.get('content', 'No content available')
                    url = r.get('url', 'No URL available')
                    extracted_data.append(f"{i+1}. {content}\nURL: {url}")
                else:
                    extracted_data.append(f"{i+1}. {str(r)}")
            
            result_str = "\n\n".join(extracted_data)
            print("Extracted data:", result_str)
            return f"Search results for '{input_query}':\n{result_str}"
        
        return f"Search results for '{input_query}':\n{str(results)}"
    except Exception as e:
        print(f"Error in research agent: {e}")
        return f"Error searching for '{input_query}': {str(e)}"

def answer_drafting_agent(context: str) -> str:
    try:
        result = chat_chain.invoke({"input": context})
        return result['text']
    except Exception as e:
        print(f"Error in drafting agent: {e}")
        return f"Failed to generate answer. Error: {str(e)}"

from typing import TypedDict

class GraphState(TypedDict):
    query: str
    research_data: str
    drafted_answer: str

# Node 1: Run Research Agent
def run_research_agent(state: GraphState) -> GraphState:
    query = state["query"]
    research_data = research_agent(query)
    return {"query": query, "research_data": research_data, "drafted_answer": ""}

# Node 2: Run Drafting Agent
def run_drafting_agent(state: GraphState) -> GraphState:
    context = state["research_data"]
    drafted_answer = answer_drafting_agent(context)
    return {**state, "drafted_answer": drafted_answer}

# Define the graph
workflow = StateGraph(GraphState)
workflow.add_node("research", run_research_agent)
workflow.add_node("draft", run_drafting_agent)
workflow.set_entry_point("research")
workflow.add_edge("research", "draft")
workflow.add_edge("draft", END)

# Compile the graph
app = workflow.compile()

if __name__ == "__main__":
    while True:
        user_query = input("Enter your research topic or type 'exit': ")
        if user_query.lower() == "exit":
            break
        result = app.invoke({"query": user_query, "research_data": "", "drafted_answer": ""})
        print("\nFinal Drafted Answer:\n")
        print(result["drafted_answer"])
