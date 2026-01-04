# gemini api and models using OpenAI sdk tool
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Load API key from environment
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)
response = client.chat.completions.create(
    model='gemma-3-12b-it',
    messages=[
        {
            "role":"system",
            "content" : "You are an expert in Maths and only answer mathematics related questions if the query is not related to maths just say sorry and do not answer that"
        },
        {
            "role" : "user",
            "content" : "Give a burger recipe"
        }
    ]
)

print(response.choices[0].message.content)

# models = client.models.list()
# for model in models:
#     print(model.id)