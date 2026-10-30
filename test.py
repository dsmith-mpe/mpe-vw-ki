from openai import OpenAI
import json
import os
from dotenv import load_dotenv


load_dotenv()
# API configuration
api_key = os.getenv("API_KEY") # Replace with your API key
base_url = "https://chat-ai.academiccloud.de/v1"
model = "qwen3.5-397b-a17b" # Choose any available model

# Start OpenAI client
client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

# Get response
chat_completion = client.chat.completions.create(
        messages=[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"How tall is the Eiffel tower?"},{"role":"assistant","content":"The Eiffel Tower stands at a height of 324 meters (1,063 feet) above ground level. However, if you include the radio antenna on top, the total height is 330 meters (1,083 feet)."},{"role":"user","content":"Are there restaurants?"}],
        model= model,
    )

# Print full response as JSON
print(chat_completion.choices[0].message.content)
