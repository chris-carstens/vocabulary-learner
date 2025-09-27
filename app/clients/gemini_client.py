import google.generativeai as genai
from app.settings import GEMINI_API_KEY

class GeminiCLient:
    def __init__(self, model: str = "gemini-2.5-flash"):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = model
        self.client = genai.GenerativeModel(self.model)

    def generate_text(self, prompt: str) -> str:
        response = self.client.generate_content(prompt)
        return response.text if response and response.text else ""

    def get_words_by_topic(self, topic: str, n: int, sent_words: set, language: str = 'italian') -> list:
        sent_words_list = ', '.join(sent_words) if sent_words else 'nessuna'
        prompt = (
            f"Elenca {n} parole {language} diverse e comuni relative al tema '{topic}', "
            f"escludendo le seguenti parole già inviate: {sent_words_list}. "
            f"Includi la traduzione in inglese per ogni parola, nel formato 'parola: traduzione'. "
            f"Rispondi solo con una lista separata da virgole, senza numeri o spiegazioni."
        )
        text = self.generate_text(prompt)
        words = [w.strip() for w in text.split(',') if w.strip()]
        words = [w for w in words if w not in sent_words]
        return words[:n]
