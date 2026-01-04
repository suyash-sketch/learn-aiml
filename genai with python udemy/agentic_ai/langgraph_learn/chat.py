from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    # model_provider="gemini"
)

class State(TypedDict):
    messages : Annotated[list, add_messages]

def chatbot(state : State):
    response = llm.invoke(state.get("messages"))
    return { "messages" : [response] }

def samplenode(state : State):
    print("\n\nInside the samplenode node", state)
    return { "messages" : ["Sample Message Appended"] }


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("samplenode",samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)


graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages" : ["Hi, My name is Suyash"]}))
print("\n\nUpdated State", updated_state)

# initially == state = { "messages" : ["hey there"]}
# node runs chatbot(state : ["hey there"]) --> ["Hii, this is message from the ChatBot"]
# now == state = { "messages" : ["hey there", "Hii, this is message from the ChatBot"] }
