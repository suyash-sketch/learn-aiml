from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.mongodb import MongoDBSaver

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

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot",chatbot)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


graph = graph_builder.compile()

def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)


DB_URL = 'mongodb://admin:suyashk1305@localhost:27017'
with MongoDBSaver.from_conn_string(DB_URL) as checkpointer:

    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer)

    config = {
        "configurable" : {
            "thread_id" : "suyash"
        }   
    }


    for chunk in graph_with_checkpointer.stream(
        State({"messages" : ["I am learning langgraph"]}), 
        config,
        stream_mode='values'
        ):
            chunk['messages'][-1].pretty_print()


# initially == state = { "messages" : ["hey there"]}
# node runs chatbot(state : ["hey there"]) --> ["Hii, this is message from the ChatBot"]
# now == state = { "messages" : ["hey there", "Hii, this is message from the ChatBot"] }    