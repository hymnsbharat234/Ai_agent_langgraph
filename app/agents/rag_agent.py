from app.vectorstore.chroma_store import vector_store


def rag_agent(state):

    docs = vector_store.similarity_search(
        state["question"],
        k=4,
    )

    state["retrieved_docs"] = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return state