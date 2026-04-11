from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "user", "content": "What is the largest mammal?"},
        {"role": "user", "content": "Weather in berlin? 05.apr.2026"},

    ],    
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None
)
for chunk in response:
    print(chunk.choices[0].delta.content or "", end="")