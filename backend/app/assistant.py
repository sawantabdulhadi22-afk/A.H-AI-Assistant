import os
from openai import OpenAI

from app.config import OPENAI_API_KEY, APP_NAME

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


def chat_with_ai(prompt: str) -> str:
    if not client:
        return (
            f"Hello, I am {APP_NAME}. I am ready to help. "
            "Add your OpenAI API key in the .env file to enable full AI responses."
        )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are A.H AI Assistant, a smart personal AI assistant. "
                    "Be helpful, concise, and professional."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=500,
    )

    return response.choices[0].message.content
