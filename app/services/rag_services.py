from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

from app.vectorstore.chroma_store import vector_store
from app.vectorstore.loader import load_documents


class RAGService:

    def ingest(self, filepath: str):

        documents = load_documents(filepath)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )

        chunks = splitter.split_documents(documents)

        vector_store.add_documents(chunks)

        return len(chunks)


rag_service = RAGService()