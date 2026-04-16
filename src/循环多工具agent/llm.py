from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
        api_key=api_key,
        base_url="https://aihubmix.com/v1"
    )
def call_llm(prompt):

    response = client.chat.completions.create(
        model="coding-minimax-m2.5-free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content