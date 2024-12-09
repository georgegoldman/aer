
from typing import Optional
from dotenv import load_dotenv
import os
import google.generativeai as genai #type: ignore

load_dotenv()

# print(os.getenv("VARSCON_Test"))


def get_chatgpt_response(context: Optional[str], message: str) -> str:
    api_key = os.getenv("AI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    messages = []
    if context:
        messages.append({"role": "system", "content": context})
    messages.append({"role": "user", "content": message})

    try:
        completion = model.generate_content(message)
        response = completion.text
        return response #type: ignore
    except Exception as e:
        return f"Error: {str(e)}" #type: ignore