from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,TextLoader,Docx2txtLoader
)

def load_documents(path:str):
    extension=Path(path).suffix.lower()

    if extension==".pdf":
        loader=PyPDFLoader(path)
    elif extension==".txt":
        loader=TextLoader(path)
    elif extension==".docx":
        loader=Docx2txtLoader(path)
    else:
        raise ValueError("Unsupported file")

    return loader.load()