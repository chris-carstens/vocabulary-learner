# Vocabulary Learner

A tool to expand your vocabulary by sending words on specific topics via Telegram.

## Features

- Fetches words by topic using the Gemini language model.
- Sends words to a Telegram chat.
- Avoids duplicate words.
- Supports daily automated delivery.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/vocabulary-learner.git
   cd vocabulary-learner
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

## Adding a New Topic

When adding a new topic, update the `words_sent.json` file with the topic key and an empty list:
```json
{
  "new_topic": []
}
```

## Usage

- **Manual Sending**: Use the `/send` endpoint.
- **Automated Delivery**: Words are sent daily at 9:00 AM (configurable in `main.py`).

## License

MIT License.
## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.
