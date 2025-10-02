import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load PDFs
pdf_dir = os.getenv("PDF_DIRECTORY", "./pdfs")
loader = DirectoryLoader(pdf_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Create embeddings and store in ChromaDB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)

print(f"✓ Ingested {len(chunks)} chunks from {len(documents)} pages")
