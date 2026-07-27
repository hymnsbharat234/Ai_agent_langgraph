from app.tools.tavily_search import search_web


def web_agent(state):

    context = search_web(
        state["question"]
    )

    state["retrieved_docs"] = context

    return state