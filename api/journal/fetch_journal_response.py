import os
from dotenv import load_dotenv
from variables.prompt_vars import SYSTEM_PROMPT, MODEL, MAX_TOKENS, TEMPERATURE
from groq import Groq

load_dotenv()

def fetch_journal_response(data):
    """Fetches the journal response for a given journal entry from an API endpoint.

    Args:
        data: A dictionary containing the journal entry.

    Returns:
        A dictionary containing the journal response.
    """
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    chat_history = [SYSTEM_PROMPT]
    user_input = data
    chat_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model=MODEL,
        messages=chat_history,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )
    return {'message': response.choices[0].message.content}
