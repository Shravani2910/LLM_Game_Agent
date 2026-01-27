import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def think(context: dict) -> str:
    observation = context["observation"]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  
        messages=[
            {"role": "system", "content": "You are an intelligent game explorer agent."},
            {"role": "user", "content": f"Observation: {observation}\nWhat should I do next?"}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()
