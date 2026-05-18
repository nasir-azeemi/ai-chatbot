import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Token budget (leave some room for the response)
MAX_TOKENS = 4096

messages = []
token_count = 0

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

    # Make the API call
    try:
        # 2. Send the ENTIRE history to the model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            # config=types.GenerateContentConfig(
            #     max_output_tokens=1024
            # )
        )

        # Update token count and check if we're approaching the limit
        token_count += response.usage_metadata.total_token_count

        # 3. Extract the response
        bot_response = response.text

        print(f"Bot: {bot_response}\n")

        # 4. Add the bot's response to history so it remembers what it said
        messages.append(types.Content(
            role="model",
            parts=[types.Part.from_text(text=bot_response)]
        ))

    except Exception as e:
        print(f"[Error] {e}")
        # Remove the first user message to free up tokens and try again
        removed = messages.pop(0)
        removed_message_token_count = client.models.count_tokens(
            model="gemini-2.5-flash", contents=removed
        )
        token_count -= removed_message_token_count.total_tokens
        print("Removed the oldest message to free up tokens. Please try again.")
