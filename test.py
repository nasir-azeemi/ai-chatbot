import os
from dotenv import load_dotenv
from google import genai


# Load environment variables from .env file
load_dotenv()


client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Generate text from a prompt
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain the difference between an AI Engineer and a Software Engineer in one sentence."
)

print(response.text)

# print(response.choices[0].message.content)
