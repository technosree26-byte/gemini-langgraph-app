"""
Gemini translation service.
"""

import google.generativeai as genai

from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


class GeminiTranslator:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:

        prompt = f"""
You are a professional translator.

Translate the following text.

Source Language:
{source_language}

Target Language:
{target_language}

Text:
{text}

Only return the translated text.
"""

        response = self.model.generate_content(prompt)

        return response.text.strip()