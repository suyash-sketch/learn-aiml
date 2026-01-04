
from google import genai
from dotenv import load_dotenv
# Load API key from environment


load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain types of AI in 30 words"
)

print(response)