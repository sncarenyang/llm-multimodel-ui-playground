import os
from openai import OpenAI
from config import OPENAI_MODEL


def ask_openai(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "Error: OPENAI_API_KEY is not set."

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
