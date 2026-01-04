from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

client = Client(
    host= "http://localhost:11434",
)

@app.post('/chat')
def chat( message: str = Body(..., description="The Message") ):
    response = client.chat(model='llama3.2:1b', 
                messages=[
                    {"role" : "user", "content" : message}
                ])
    return {"response" : response.message.content}
