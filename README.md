# ai-chatbot

As a software engineer diving into AI, I had this assumption that chatbots were fundamentally different from traditional applications. They seemed almost magical in how they maintained context and responded intelligently.

This is my attempt on building one: a chatbot is just a conversation where you're manually managing state (doesnt have to be this way with gemini), the same way you'd manage a shopping cart or user session in a web app. The "AI" part is just one API call. Everything else is good old-fashioned software engineering.

Building intelligent applications isn't about learning an entirely new paradigm. It's about understanding how to orchestrate LLM APIs within the patterns you already know. The earlier you start, the more natural this becomes.

## How to start

1. Create and activate a virtual environment if you do not already have one.
2. Install the dependencies used by the scripts:

```bash
pip install google-genai python-dotenv
```

3. Add your Gemini API key to a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

4. Run one of the chatbot scripts:

```bash
python chatbot_manual_history.py
python chatbot_auto_history.py
python chatbot_sliding_window.py
```

`test.py` is a simple one-shot example you can run the same way.
