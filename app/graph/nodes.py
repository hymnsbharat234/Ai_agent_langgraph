from app.graph.state import GraphState
from app.services.llm import llm
from app.vectorstore.chroma_store import vector_store
from langchain_core.documents import Document
from app.tools.tavily_search import search_web


def planner_node(state:GraphState):
    question=state["question"].lower()
    web_keywords=[
        "today",
        "latest",
        "news",
        "current",
        "recent",
        "2026",
        "live"
    ]
    if any (keyword in question for keyword in web_keywords):
        state["route"]="web"
    else:
        state["route"]="rag"

        return state
    print("Planner node")

    return state

def retrieve_node(state: GraphState) -> GraphState:
    docs: list[Document] = vector_store.similarity_search(state["question"], k=4)
    context = "\n\n".join(doc.page_content for doc in docs)
    state["retrieved_docs"] = context
    return state

def generate_node(state):

    prompt = f"""
You are an expert AI Research Assistant.
Answer ONLY from the provided context.
If the answer is unavailable,
say you don't know.

Question:
{state['question']}

Context:
{state['retrieved_docs']}
"""

    response = llm.invoke(prompt)

    state["answer"] = response.content

    return state




def web_search_node(state):

    print("Searching Web...")

    context = search_web(
        state["question"]
    )

    state["retrieved_docs"] = context

    return state

def route_question(state:GraphState):
    return state["route"]