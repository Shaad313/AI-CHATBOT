from __future__ import annotations

from google.genai import errors

from config import load_settings, setup_logging
from chatbot import GeminiChatbot
from utils.helpers import get_non_empty_input, print_ai_message, print_error, print_welcome


def main() -> None:
    """Run the command-line chatbot application."""
    settings = load_settings()
    setup_logging(settings.log_file)

    chatbot = GeminiChatbot(settings=settings)
    print_welcome(settings.model_name)

    while True:
        user_input = get_non_empty_input("You: ")

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Chatbot: Goodbye! Thanks for chatting.")
            break

        try:
            response = chatbot.send_message(user_input)
        except errors.ClientError as exc:
            error_text = str(exc)
            status_code = str(getattr(exc, "status_code", ""))
            if status_code == "429" or "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                print_error(
                    "Gemini quota or rate limit reached. Wait a minute and try again, "
                    "or create/check your API key in Google AI Studio."
                )
            elif status_code == "400" or "400" in error_text:
                print_error("Gemini rejected the request. Check your model name and API key setup.")
            elif status_code in {"401", "403"} or "401" in error_text or "403" in error_text:
                print_error("Gemini authentication failed. Check that GEMINI_API_KEY is correct.")
            else:
                print_error(f"Gemini API error: {exc}")
            chatbot.logger.exception("Gemini API request failed: %s", exc)
            continue
        except Exception as exc:
            print_error("I could not get a response from Gemini. Please try again.")
            chatbot.logger.exception("Chatbot request failed: %s", exc)
            continue

        print_ai_message(response)


if __name__ == "__main__":
    main()
