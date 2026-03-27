import os
from dotenv import load_dotenv
import google.generativeai as genai
from .prompt import ANTIGRAVITY_PROMPT

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    # Use a mock or warn if no API key is set
    print("WARNING: GEMINI_API_KEY not found in environment.")

model = genai.GenerativeModel('gemini-1.5-flash')

async def humanize_text(text: str) -> str:
    \"\"\"
    Uses Gemini to humanize the input text based on the Antigravity laws.
    \"\"\"
    if not text or len(text.strip()) == 0:
        return ""

    response = await model.generate_content_async(
        f"{ANTIGRAVITY_PROMPT}\n\nInput: {text}\n\nAntigravity Result:"
    )
    
    return response.text.strip()
