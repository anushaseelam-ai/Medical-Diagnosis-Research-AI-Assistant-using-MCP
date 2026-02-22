# tools/summarizer.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = AzureChatOpenAI(  
    azure_endpoint=os.getenv["AZURE_OPENAI_ENDPOINT"],
    api_key=os.getenv["AZURE_OPENAI_API_KEY"],
    api_version="2024-02-15-preview"
)

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following medical abstract:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a medical research summarizer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
