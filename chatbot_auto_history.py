
from dotenv import load_dotenv
import os
from google import genai


load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")

print("Chatbot ready! Type 'quit' or 'exit' to end the conversation.\n")


while True:

    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    response = chat.send_message(user_input)

    bot_response = response.text
    print(f"Bot: {bot_response}\n")


for message in chat.get_history():
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)
