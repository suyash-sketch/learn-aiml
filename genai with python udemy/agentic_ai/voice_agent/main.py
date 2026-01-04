import asyncio
import speech_recognition as sr
from openai import OpenAI, AsyncOpenAI
from openai.helpers import LocalAudioPlayer
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)
async_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

async def tts(speech : str):
    async with async_client.audio.speech.with_streaming_response.create(
        model='gemini-2.5-flash-native-audio-dialog',
        voice='Kore',
        instructions="Speak in a cheerful and positive voice",
        input=speech,
        response_format='pcm'
    ) as response:
        await LocalAudioPlayer().play(response)
        
        
def main():
    r = sr.Recognizer() # speech to text
    
    with sr.Microphone() as source: #mic access
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        
        print("Speak something....")
        audio = r.listen(source)
        
        print("Processing Audio....(STT)")
        stt = r.recognize_google(audio)
        print("You said...",stt)
        
        SYSTEM_PROMPT = """
        You're an expert voice agent you are given a transcript of what user has said using voice. You need to output as if you are a voice agent and whatever you speak will be converted back to audio using ai and played back to user
        """
        
        response = client.chat.completions.create(
            model='gemini-2.5-flash-lite',
            messages=[
                {"role" : "system","content":SYSTEM_PROMPT },
                {'role':"user","content": stt},
            ]
        )
        
        print("AI Repsonse:", response.choices[0].message.content)
        asyncio.run(tts(speech=response.choices[0].message.content))
        
main()
        