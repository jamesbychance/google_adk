import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def local_rag_search(query: str):
    """Search through locally stored PDF documents."""
    persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    results = vectorstore.similarity_search(query, k=5)
    return {"results": [{"content": doc.page_content, "metadata": doc.metadata} for doc in results]}
