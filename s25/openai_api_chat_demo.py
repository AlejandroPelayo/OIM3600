import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def ge_topenai_response(user_prompt):
    """get a repspinse from OpenAis text generation API"""
    system_prompt = "You are a very helpful assistant for learning python"

    completion = client.chat.completions.create(
        model="gpt-4o"
        messages=[
            {
                "role": "system"
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )
    response = completion.choices[0].message.content
    return response

def main():
    while True:
        user_prompt = input("What is your question? \n")
        response = ge_topenai_response(user_prompt)
        print(response)

main()
