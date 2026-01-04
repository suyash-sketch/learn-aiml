from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from langchain_ollama import OllamaEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
openai_client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)


#vector embedding
embedding_model = OllamaEmbeddings(
    base_url='http://localhost:11434',
    model='nomic-embed-text'
)

vector_db = QdrantVectorStore.from_existing_collection(
    url='http://localhost:6333',
    collection_name='learning_rag',
    embedding=embedding_model
)

#take user input 
user_query = input("Ask something: ")

# Relevant chunks from vector db
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" 
                        for result in search_results])

SYSTEM_PROMPT = f"""
    You are a helpful AI assistant who answers user query based on available context retrieved from a PDF file along with page_contents and page number.

    You should only answer the user based on the following context and navigate the user to open the right page number to know more

    Context:
    {context}
"""

response = openai_client.chat.completions.create(
    model='gemini-2.5-flash-lite',
    messages=[
        {"role":"system", "content" : SYSTEM_PROMPT},
        {"role":"user", "content":user_query}
    ]
)

print(f"🤖: {response.choices[0].message.content}")