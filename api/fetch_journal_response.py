"""Fetches the journal response for a given journal entry from groqcloud api endpoint."""
from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

async def fetch_journal_response(data):
    """Fetches the journal response for a given journal entry from an api endpoint.

    Args:
        data: A dictionary containing the journal entry.

    Returns:
        A dictionary containing the journal response.
    """
    print("aaaaa", API_KEY)
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{
            "role": "user",
            "content": data
        }]
    }
    headers = {
        'Authorization': 'Bearer `${API_KEY}`',
        'Content-Type': 'application/json'
    }
    response = await requests.post('https://api.groq.com/openai/v1/chat/completions', json=data, headers=headers)
    print(request)
    print(response)
    # response = request.post('https://api.groq.com/openai/v1/chat/completions', json=data)
    # print(response)
    return {'message': 'Journal response fetched successfully'}

