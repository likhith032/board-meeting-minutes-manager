import os
import datetime
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_minutes_summary(meeting_notes):
    """
    Day 3 Task: Process notes and return structured JSON
    """
    # 1. Validation
    if not meeting_notes:
        return {"error": "meeting_notes are required", "status": 400}

    # 2. Load Day 2 Template
    # Adjust path if your prompts folder is in a different spot
    prompt_path = os.path.join('app', 'prompts', 'minutes_template.txt')
    with open(prompt_path, 'r') as file:
        template = file.read()

    full_prompt = template.replace("{{meeting_notes}}", meeting_notes)

    # 3. Groq API Call
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a professional secretary."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.5,
    )

    # 4. Return Structured JSON
    return {
        "summary": completion.choices[0].message.content,
        "generated_at": datetime.datetime.now().isoformat(),
        "status": "success"
    }