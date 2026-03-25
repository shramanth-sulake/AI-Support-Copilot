from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_response(query: str, context: list[str], history: list[dict]):
    context_text = "\n\n".join(context)

    messages = []

    # add history
    for msg in history:
        messages.append(msg)

    # add current query with context
    messages.append({
        "role": "user",
        "content": f"""
Use the context to answer.

Context:
{context_text}

Question:
{query}
"""
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content