#  AI Chatbot using Python and Google Gemini API

A professional command-line AI chatbot built with Python and the Google Gemini API. The app accepts natural-language prompts, maintains conversation context during the current session, logs conversations, and keeps secrets out of source control with environment variables.

## Features

- Clean command-line chat interface
- Google Gemini API integration with the official `google-genai` SDK
- Multi-turn conversation memory for the active session
- Secure API key loading from a `.env` file
- System prompt support through `prompts/system_prompt.txt`
- Conversation and error logging
- Modular, portfolio-friendly Python project structure
- Basic automated tests

## Project Structure

```text
ai-chatbot/
├── app.py
├── chatbot.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── prompts/
│   └── system_prompt.txt
├── logs/
│   └── .gitkeep
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── tests/
    └── test_chatbot.py
```

## Requirements

- Python 3.12+
- A free Google Gemini API key from Google AI Studio
- Visual Studio Code or any Python editor

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/llm-ai-chatbot.git
cd llm-ai-chatbot
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create your environment file:

```bash
copy .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

5. Add your Gemini API key to `.env`:

```env
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-2.0-flash
GEMINI_TEMPERATURE=0.7
```

## Usage

Run the chatbot:

```bash
python app.py
```

Type your questions in the terminal. Use `exit`, `quit`, or `bye` to end the session.

## Troubleshooting

If you see a quota or rate-limit error, Gemini returned HTTP `429`. Wait a minute and try again, or create a fresh API key in Google AI Studio and confirm the selected model has free-tier quota available for your account.

If you see an authentication error, check that `.env` contains a valid `GEMINI_API_KEY` and no extra quotes or spaces.

## Testing

Run the test suite:

```bash
pytest
```

## Notes

- Do not commit your `.env` file.
- Conversation logs are written to `logs/chatbot.log` at runtime and ignored by Git.
- The chatbot keeps memory only while the program is running.

## Portfolio Highlights

This project demonstrates API integration, environment management, prompt engineering, modular Python design, logging, exception handling, and test organization.
