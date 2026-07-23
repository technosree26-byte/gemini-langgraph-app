"""
Gemini translation service.
"""

import google.generativeai as genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL


# Configure Gemini once when the module is imported
genai.configure(api_key=GEMINI_API_KEY)


class GeminiTranslator:
    """
    Wrapper around the Gemini model for translation tasks.
    """

    def __init__(self):
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        print("Using Gemini model:", GEMINI_MODEL)
        
    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:
        """
        Translate text from the source language to the target language.
        """

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

        try:
            response = self.model.generate_content(prompt)

            # Safety check for empty responses
            if not response or not getattr(response, "text", None):
                raise RuntimeError("Gemini returned an empty response.")

            return response.text.strip()

        except Exception as e:
            raise RuntimeError(f"Gemini API error: {e}")