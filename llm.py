import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY was not found in the .env file.")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=api_key,
)


def summarize_text(text: str) -> str:
    if not text.strip():
        raise ValueError("Text cannot be empty.")

    prompt = f"""
You are a PDF summarization assistant.

Summarize the following text.

Requirements:
- Use clear headings
- Use concise bullet points
- Preserve important names, facts, dates, and definitions
- Do not add information that is not present
- Remove unnecessary repetition

Text:
{text}
"""

    response = llm.invoke(prompt)

    return str(response.content)