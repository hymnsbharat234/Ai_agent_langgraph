from langchain_chroma import Chroma
from app.vectorstore.embeddings import embedding
vector_store=Chroma(
    collection_name="research_documents",
    embedding_function=embedding,
    persist_directory="./chroma.db"
)