from openai import OpenAI
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()



client = OpenAI(api_key=os.getenv("VARSCON_Test"))



def get_chatgpt_response(context: Optional[str], message: str) -> str:
    messages = []
    if context:
        messages.append({"role": "system", "content": context})
    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL"), #type: ignore
            messages=messages #type: ignore
        )
        return response.choices[0].message.content #type: ignore
    except Exception as e:
        return f"Error: {str(e)}" #type: ignore