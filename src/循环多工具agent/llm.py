from openai import OpenAI
client = OpenAI(
        api_key="sk-lFB02hEtWgkT9Cy38cE6EaBdA64644Bc96E447F93772C7Cf",
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