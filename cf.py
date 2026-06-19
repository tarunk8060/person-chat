import os
from dotenv import load_dotenv
from google import genai
import streamlit as st

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

def classify_persona(message):
    prompt = f"""
Classify this user message into exactly one category:

1. Technical Expert
2. Frustrated User
3. Business Executive
4. General User

Return ONLY the category name.

Message:
{message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
