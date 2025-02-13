import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
AIPROXY_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

def parse_task(task_description):
    """Uses IITM Proxy API to process the task description."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AIPROXY_TOKEN}",
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": task_description}],
        "temperature": 0.5
    }

    try:
        response = requests.post(AIPROXY_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise error for 400+ HTTP failures

        # Extract the message content correctly
        return response.json()["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"API Error: {str(e)}"
