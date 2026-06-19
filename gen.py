import os
from dotenv import load_dotenv
from google import genai
import streamlit as st

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

def generate_response(persona, query, context):
    context_text = "\n".join(context[0])

    prompt = f"""
You are an AI customer support agent.

Customer Persona:
{persona}

Knowledge Base Context:
{context_text}

User Question:
{query}

Instructions:
- Technical Expert → detailed technical explanation
- Frustrated User → empathetic and simple
- Business Executive → short and business-focused
- General User → clear normal explanation

Respond appropriately.
"""

    response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=prompt
)

    return response.text
