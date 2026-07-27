from langgraph.graph import END, StateGraph

from app.graph.nodes import (
    planner_node,
    retrieve_node,
    web_search_node,
    generate_node,
    route_question,
)
from app.graph.state import GraphState

builder = StateGraph(GraphState)

builder.add_node("planner", planner_node)
builder.add_node("retrieve", retrieve_node)
builder.add_node("web", web_search_node)
builder.add_node("generate", generate_node)

builder.set_entry_point("planner")

builder.add_conditional_edges(
    "planner",
    route_question,
    {
        "rag": "retrieve",
        "web": "web",
    },
)

builder.add_edge("retrieve", "generate")
builder.add_edge("web", "generate")
builder.add_edge("generate", END)

graph = builder.compile()