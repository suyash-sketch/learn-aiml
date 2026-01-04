import json
from openai import OpenAI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

URL = "https://api.weatherapi.com/v1/forecast.json?key=01a2ed6651dc4f008f8110535250207&q="

client = OpenAI(
    # api_key="ollama",  # Ollama doesn't require a real API key
    # base_url="http://localhost:11434/v1"
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

def get_weather(city : str):
    url = f"{URL}{city.lower()}&days=6&aqi=yes&alerts=no"
    response = requests.get(url)
    data = json.loads(response.text)
    temp = data['current']['temp_c']
    
    if response.status_code == 200:
        return f"The temperature in {city} is {temp}C"
    return "Something went wrong"


# print(get_weather("mumbai"))

available_tool = {
    "get_weather" : get_weather
}

SYSTEM_PROMPT = """You are an AI assistant. You must respond ONLY with valid JSON in this exact format:
{"step": "PLAN", "content": "your thought here"}

IMPORTANT: Return ONLY ONE valid JSON object per response. Do not include multiple JSONs or extra text.

Steps you can use:
- PLAN: for thinking steps
- TOOL: to call a tool (must include "tool" and "input" fields)
- OUTPUT: final answer to user

Available tools:
- get_weather: takes city name, returns weather info

Example for weather query:
{"step": "PLAN", "content": "User wants weather for a city"}
{"step": "TOOL", "tool": "get_weather", "input": "delhi"}
{"step": "OUTPUT", "content": "The weather in Delhi is 20C and cloudy"}
"""
print("\n\n\n")


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉🏼 ")
message_history.append(
    {'role' : 'user', 'content':user_query}
)

while True:
    response = client.chat.completions.create(
        model="llama3.2:1b",
        response_format = {"type":"json_object"},
        messages=message_history
    )
    
    raw_result = (response.choices[0].message.content)
    
    # Try to parse JSON with error handling
    try:
        parsed_result = json.loads(raw_result)
        # Handle case where API returns a list instead of a dict
        if isinstance(parsed_result, list):
            parsed_result = parsed_result[0] if parsed_result else {}
    except json.JSONDecodeError as e:
        print(f"⚠️  JSON parsing error: {e}")
        print(f"Raw response: {raw_result[:200]}...")
        print("\nTry using a larger model like llama3.2:3b or llama3.1:8b for better results.")
        break
    
    message_history.append({'role' : 'assistant', 'content' : raw_result})
    
    if parsed_result.get("step") == "START":
        print("🔥: ", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        tool_response = available_tool[tool_to_call](tool_input)
        print(f"🛠️: {tool_to_call}({tool_input}) = {tool_response} ")

        tool_response = available_tool[tool_to_call](tool_to_call)
        message_history.append({"rool" : "developer", "content" : json.dumps({"steps" : "OBSERVE", "tool":tool_to_call, "input" : tool_input, "output" : tool_response})
                                })
        continue
        
    if parsed_result.get("step") == "PLAN":
        print("🧠 :", parsed_result.get("content"))
        continue
        
    if parsed_result.get("step") == "OUTPUT":
        print("🤖 :", parsed_result.get("content"))
        break
print("\n\n\n")