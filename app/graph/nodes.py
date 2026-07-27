from app.graph.state import GraphState
from app.services.llm import llm

def planner_node(state:GraphState):
    print("Planner node")

    return state

def retrieve_node (state:GraphState):
    print("Retriver node")

    state["retrived_docs"]="No documents available yet."

    return state

def generate_node(state:GraphState):
    print("Generator Node")

    prompt=f"""You are an AI Research Assistant.
        Question:{state['question']}
        Context:{state['retrived_docs']}

        Answer clearly.
        """
    response=llm.invoke(prompt)

    state["answer"]=response.content
    return state