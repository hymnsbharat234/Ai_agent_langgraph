from langchain_huggingface import HuggingFaceEmbeddings

# No Hugging Face token is required for this public model.
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)