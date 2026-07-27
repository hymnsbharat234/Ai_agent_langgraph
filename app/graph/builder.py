from langgraph.graph import END
from langgraph.graph import StateGraph

from app.graph.nodes import (
    generate_node,
    planner_node,
    retrieve_node,
)
from app.graph.state import GraphState

builder = StateGraph(GraphState)

builder.add_node("planner", planner_node)
builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()