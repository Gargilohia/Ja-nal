"""Fetches the journal response for a given journal entry from groqcloud api endpoint."""
from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()


async def fetch_journal_response(data):
    """Fetches the journal response for a given journal entry from an api endpoint.

    Args:
        data: A dictionary containing the journal entry.

    Returns:
        A dictionary containing the journal response.
    """
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"), )
    print("aaaaa", os.environ.get("GROQ_API_KEY"))
    system_prompt = {
    "role": "system",
    "content":
    "You are a helpful assistant. You reply with very short answers."
    }
    chat_history = [system_prompt]
    user_input = data
    chat_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
    chat_history.append({
      "role": "assistant",
      "content": response.choices[0].message.content
    })
    # response = request.post('https://api.groq.com/openai/v1/chat/completions', json=data)
    # print(response)
    return {'message': 'Journal response fetched successfully'}

