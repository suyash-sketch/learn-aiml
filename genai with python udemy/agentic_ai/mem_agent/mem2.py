import json
from mem0 import Memory
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ---------------------------
# Gemini client (chat brain)
# ---------------------------
openai_client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# ---------------------------
# Mem0 configuration
# ---------------------------
config = {
    "version": "v1.0.1",

    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",  # 768-dim
            "ollama_base_url": "http://localhost:11434",
        },
    },

    "llm": {
        "provider": "ollama",
        "config": {
            "model": "llama3.2:1b",
            "ollama_base_url": "http://localhost:11434",
        },
    },

    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "collection_name": "mem0_ollama_768",
            "embedding_model_dims": 768,
        },
    },
}

mem_client = Memory.from_config(config)

print("🧠 Memory Agent Ready. Type 'exit' to quit.\n")

# ---------------------------
# Chat loop
# ---------------------------
while True:
    user_query = input("👉🏼: ").strip()
    if user_query.lower() == "exit":
        break

    # ---------------------------
    # DEBUG: list ALL memories
    # ---------------------------
    search_result = mem_client.search(
        user_id="suyash",
        query="user information",          # <-- IMPORTANT CHANGE
        limit=10
    )

    print("RAW SEARCH RESULT:", search_result)

    memories = [
        mem["memory"]
        for mem in search_result.get("results", [])
    ]

    print("🔎 Found memories:", memories)

    # ---------------------------
    # System prompt with memory
    # ---------------------------
    SYSTEM_PROMPT = f"""
You are a helpful assistant.
Here is what you know about the user from memory:
{json.dumps(memories, indent=2)}
"""

    # ---------------------------
    # Gemini response
    # ---------------------------
    response = openai_client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ]
    )

    ai_response = response.choices[0].message.content
    print("AI:", ai_response)

    # ---------------------------
    # EXPLICIT MEMORY SAVE (FACTS)
    # ---------------------------
    if "my name is" in user_query.lower():
        name = user_query.split()[-1].capitalize()
        mem_client.add(
            user_id="suyash",
            messages=[
                {
                    "role": "system",
                    "content": f"Remember this as a long-term memory: The user's name is {name}."
                }
            ]
        )

    # ---------------------------
    # DO NOT overwrite with weak extraction
    # ---------------------------
    # (Leave this disabled while learning)
    #
    # mem_client.add(
    #     user_id="suyash",
    #     messages=[
    #         {"role": "user", "content": user_query},
    #         {"role": "assistant", "content": ai_response},
    #     ]
    # )

    print("💾 Memory processing complete.\n")
