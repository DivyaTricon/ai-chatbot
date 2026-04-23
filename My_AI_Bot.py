import os
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

input_prompt = input("Enter your prompt: ")
# Get API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please set it in your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        
        {
            "role": "user",
            "content": input_prompt
        }
    ]
)

print(response.choices[0].message.content)