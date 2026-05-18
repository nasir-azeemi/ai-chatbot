import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# This list is our conversation memory
messages = []

print("Chatbot ready! Type 'quit' or 'exit' to end the conversation.\n")

while True:

    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    # 1. Add user message to our conversation history
    messages.append(types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_input)]
    ))

    # 2. Send the ENTIRE history to the model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        # config=types.GenerateContentConfig(
        #     max_output_tokens=1024
        # )
    )

    # 3. Extract the response
    bot_response = response.text

    print(f"Bot: {bot_response}\n")

    # 4. Add the bot's response to history so it remembers what it said
    messages.append(types.Content(
        role="model",
        parts=[types.Part.from_text(text=bot_response)]
    ))
