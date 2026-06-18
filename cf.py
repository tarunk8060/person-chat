import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

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
