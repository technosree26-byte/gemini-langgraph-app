from gtts import gTTS
import os
import uuid


LANGUAGE_MAP = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Tamil": "ta",
    "Chinese": "zh-CN",
    "Japanese": "ja",
}


def generate_audio(text, language):

    lang = LANGUAGE_MAP.get(language, "en")

    tts = gTTS(text=text, lang=lang)

    os.makedirs("data/output", exist_ok=True)

    filename = f"data/output/{uuid.uuid4()}.mp3"

    tts.save(filename)

    return filename
