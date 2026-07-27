from langgraph.graph import END, StateGraph
from app.agents.answer_agent import answer_agent
from app.agents.general_agent import general_agent
from app.agents.rag_agent import rag_agent
from app.agents.supervisor import supervisor
from app.agents.web_agent import web_agent

from app.graph.nodes import (
    planner_node,
    retrieve_node,
    web_search_node,
    generate_node,
    route_question,
    supervisor_router
)
from app.graph.state import GraphState

builder = StateGraph(GraphState)

builder.add_node("planner", planner_node)
builder.add_node("retrieve", retrieve_node)
builder.add_node("web_search", web_search_node)
builder.add_node("generate", generate_node)
builder.add_node("supervisor", supervisor)
builder.add_node("rag", rag_agent)
builder.add_node("web_agent", web_agent)
builder.add_node("general", general_agent)
builder.add_node("answer", answer_agent)

builder.set_entry_point("planner")
builder.add_edge("planner", "supervisor")

builder.add_conditional_edges(
    "supervisor",
    supervisor_router,
    {
        "rag": "rag",
        "web": "web_agent",
        "general": "general",
    },
)

builder.add_edge("rag", "answer")
builder.add_edge("web_agent", "answer")
builder.add_edge("general", "answer")
builder.add_edge("answer", END)

graph = builder.compile()