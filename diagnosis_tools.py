import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = AzureChatOpenAI(    
    azure_endpoint=os.getenv["AZURE_OPENAI_ENDPOINT"],
    api_key=os.getenv["AZURE_OPENAI_API_KEY"],
    api_version="2024-02-15-preview"
)
def get_diagnosis(symptoms: list[str]) -> str:
    prompt = f"Patient has symptoms: {', '.join(symptoms)}. Suggest possible medical diagnoses.suggest me a possible cure from the same"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
