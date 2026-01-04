from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import Qdrant, QdrantVectorStore
from qdrant_client import QdrantClient

pdf_path = Path(__file__).parent / "nodejs.pdf"

#Load the file in python program
loader = PyPDFLoader(pdf_path)

docs = loader.load()
# print(docs[12])

#Split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)

chunks = text_splitter.split_documents(documents=docs)


# Vector Embeddings
embedding_model = OllamaEmbeddings(
    model='nomic-embed-text',
    base_url='http://localhost:11434'
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url='http://localhost:6333',
    collection_name = "learning_rag"
)

print("Indexing of documents done....")