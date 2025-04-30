import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_fields_from_text(text):
    system_prompt = """
    You are an AI that reads contract or invoice text and returns this data as JSON:
    {
        "party_names": "",
        "payment_terms": "",
        "obligations": "",
        "deadlines": "",
        "risks": ""
    }
    """

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ],
        temperature=0.2,
    )
    
    return response.choices[0].message.content
