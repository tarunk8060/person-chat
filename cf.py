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
    msg = message.lower()

    technical_words = ["api", "token", "error", "bug", "server", "database"]
    frustrated_words = ["angry", "worst", "hate", "urgent", "immediately"]
    business_words = ["revenue", "timeline", "business", "impact", "client"]

    if any(word in msg for word in technical_words):
        return "Technical Expert"

    if any(word in msg for word in frustrated_words):
        return "Frustrated User"

    if any(word in msg for word in business_words):
        return "Business Executive"

    prompt = f"""
Classify into one category only:
Technical Expert
Frustrated User
Business Executive
General User

Message:
{message}

Return category only.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
