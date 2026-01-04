from dotenv import load_dotenv
from typing import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from openai import OpenAI
# from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)


class State(TypedDict):
    user_query : str
    llm_output : Optional[str]
    is_good : Optional[bool]

def chatbot_gemini_lite(state : State):
    print("chatbot_gemini_lite node", state)
    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        messages=[
            { "role" : "user", "content" : state.get("user_query") } 
        ]
    )

    state['llm_output'] = response.choices[0].message.content
    return state


def chatbot_gemini_flash(state : State):
    print("chatbot_gemini_flash node", state)
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            { "role" : "user", "content" : state.get("user_query") }
        ]
    )

    state['llm_output'] = response.choices[0].message.content
    return state

def endnode(state : State):
    print("end node", state)
    return state

def evaluate_response(state : State) -> Literal['chatbot_gemini_flash', 'endnode']:
    print("evaluate_response node", state)
    if False:
        return "endnode"
    
    return "chatbot_gemini_flash"

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot_gemini_lite", chatbot_gemini_lite)
graph_builder.add_node("chatbot_gemini_flash", chatbot_gemini_flash)
graph_builder.add_node("endnode", endnode)

graph_builder.add_edge(START, 'chatbot_gemini_lite')    
graph_builder.add_conditional_edges('chatbot_gemini_lite', evaluate_response)
graph_builder.add_edge('chatbot_gemini_flash', 'endnode')
graph_builder.add_edge('endnode', END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_query" : "Hey, what is 2 + 2 ?"}))

print(updated_state)