import json
from pathlib import Path
from app.clients.gemini_client import GeminiCLient
from app.clients.telegram_client import TelegramClient

WORDS_SENT_FILE = Path('app/words_sent.json')
llm_client = GeminiCLient()
telegram_client = TelegramClient()

def load_words_sent():
    if WORDS_SENT_FILE.exists():
        with open(WORDS_SENT_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_words_sent(data):
    with open(WORDS_SENT_FILE, 'w') as f:
        json.dump(data, f)


async def send_words(language, topics, n):
    sent_words = load_words_sent()
    for topic in topics:
        sent_words_topic = sent_words.get(topic, [])
        words = llm_client.get_words_by_topic(topic, n, sent_words_topic, language=language)
        sent_words_topic.extend([word.split(':')[0].strip() for word in words])
        save_words_sent(sent_words)

        # Format the message with a nice style and context
        messages = [f"📚 {language.capitalize()} Vocabulary - Topic: {topic.capitalize()}"]
        for word in words:
            italian, english = word.split(': ')
            messages.append(f"🔹 {italian.strip()} - {english.strip()}")
        text = '\n'.join(messages)

        # Send the formatted message
        await telegram_client.send_message(text)
