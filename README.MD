# Vocabulary Learner

A tool to expand your vocabulary by sending words on specific topics via Telegram.

## Features

- Fetches words by topic using the Gemini language model.
- Sends words to a Telegram chat.
- Avoids duplicate words.
- Supports daily automated delivery.

## Requirements

- Python 3.10 or higher

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/chris-carstens/vocabulary-learner
   cd vocabulary-learner
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   Create a `.env` file inside app directory and add the following variables:
   ```
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   TELEGRAM_CHANNEL_ID=your-telegram-channel-id
   GEMINI_API_KEY=your-gemini-api-key
   ```
   Replace `your-telegram-bot-token`, `your-telegram-channel-id`, and `your-gemini-api-key` with your actual credentials.

5. Set constants in `main.py`:
   Open the `app/main.py` file and configure the following constants to suit your needs:
   ```python
   LANGUAGE = 'italian'
   TOPICS = ['food']
   N_WORDS = 5
   SCHEDULED_TIME_HOUR = 9
   SCHEDULED_TIME_MINUTE = 0
   TIMEZONE = pytz.timezone("UTC")
   ```

6. Run the app:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## Adding a New Topic

When adding a new topic, update the `words_sent.json` file with the topic key and an empty list:
```json
   {
   "new_topic": []
   }
```
This file tracks sent words to avoid duplicates.

## Usage

- **Manual Sending**: Use the `/send` endpoint.
- **Automated Delivery**: Words are sent daily at 9:00 AM UTC(configurable in `main.py`).

## License

MIT License.

## License

This project is licensed under the MIT License.
