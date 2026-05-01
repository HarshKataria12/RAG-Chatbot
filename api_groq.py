from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def ask_groq(question, collection):
    # Step 1: get chunks from ChromaDB
    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    context = "\n\n".join(results["documents"][0])

    # Step 2: send to Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"""Answer ONLY based on:
Context: {context}
If answer not in context, say 'I dont know based on this document'.
"""},
            {"role": "user", "content": question}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
    )
    return response.choices[0].message.content