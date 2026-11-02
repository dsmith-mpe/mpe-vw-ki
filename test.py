from openai import OpenAI
from collections import deque
import os
from dotenv import load_dotenv


load_dotenv()
# API configuration
api_key = os.getenv("API_KEY")  # Replace with your API key
base_url = "https://chat-ai.academiccloud.de/v1"
model = "qwen3.5-397b-a17b"  # Choose any available model

# Start OpenAI client
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)


MAX_SIZE = 10
chat_history = deque(maxlen=MAX_SIZE)

SYSTEM_PROMPT = {"role": "system", "content": "You are a helpful assistant"}

print("Chat started! Type 'exit' or 'quit' to stop.\n")

while True:
    prompt = input("You: ")

    # Exit condition
    if prompt.lower() in ("exit", "quit"):
        print("Chat ended.")
        break

    # Add user message
    chat_history.append({
        "role": "user",
        "content": prompt
    })

    # Build conversation context
    messages = [
        SYSTEM_PROMPT,
        *chat_history
    ]

    # Get assistant response
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
    )

    response = chat_completion.choices[0].message.content

    print(f"\nAssistant: {response}\n")

    # Store assistant response
    chat_history.append({
        "role": "assistant",
        "content": response
    })
