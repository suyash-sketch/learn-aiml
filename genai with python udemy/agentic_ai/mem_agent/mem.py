import json
from dotenv import load_dotenv
from mem0 import Memory
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

openai_client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEO4J_URL = os.getenv("NEO_CONNECTION_URI")
NEO_USERNAME = os.getenv("NEO_USERNAME")
NEO_PASSWORD = os.getenv("NEO_PASSWORD")

config = {
    "version" : "v1.0.1",
    "embedder" : {
        "provider" : "ollama",
        "config" : {
            "model" : "nomic-embed-text",
            "ollama_base_url" : "http://localhost:11434",
        },
    },
    "llm" : {
        "provider" : "ollama",
        "config" : {
            "model" : "llama3.2:1b",
            "ollama_base_url" : "http://localhost:11434",
        },
    },
    "graph_store" : {
        "provider" : "neo4j",
        "config" : {
            "url" : "neo4j+s://51060a18.databases.neo4j.io",
            "username" : "neo4j",
            "password" : "c7ohJ2f3KeDGCa9Rwr0RrHJ_1foBCg8GFRDAAVMOi-s"
        }
    },
    "vector_store" : {
        "provider" : "qdrant",
        "config" : {
            "host" : "localhost",
            "port" : 6333,
            "collection_name": "mem0_ollama_768",
            "embedding_model_dims" : 768
        },
    },
    # "llm" : {
    #     "provider" : "openai",  # mem0 does not support gemini or vertexai provider
    #     "config" : {
    #         "api_key" : GEMINI_API_KEY,
    #         "model" : "gemini-2.5-flash",
    #         "site_url": "https://generativelanguage.googleapis.com/v1beta/openai"

    #     },
    # },
}

mem_client = Memory.from_config(config)

while True:

    user_query = input("👉🏼: ")
    
    search_memory = mem_client.search(query = user_query, user_id="suyash")
    
    memories = [
        f"ID: {mem["id"]}\nMemory: {mem['memory']} " for mem in search_memory.get("results", [])
    ]
    
    print("Found memories", memories)
    
    SYSTEM_PROMPT = f"""
    Here is the context about the user {json.dumps(memories)}
    """    
    response = openai_client.chat.completions.create(
        model='gemini-2.5-flash-lite',
        messages=[
            {
                        "role": "system",
                        "content": (
                            "This is important long-term user information. "
                            "Extract and remember stable facts only."
                        )
                    },
            { "role" : "system", "content" : SYSTEM_PROMPT },
            { "role" : "user", "content" : user_query }
        ]
    )
    
    ai_response = response.choices[0].message.content
    
    print("AI:", ai_response)
    
    mem_client.add(
        user_id="suyash",
        messages=[
            { "role" : "user", "content" : user_query },
            { "role" : "assistant", "content" : ai_response }
        ]
    )
    
    print("Memory has been saved....")
