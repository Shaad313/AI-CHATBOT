from __future__ import annotations


def print_welcome(model_name: str) -> None:
    print("=" * 60)
    print("LLM AI Chatbot powered by Google Gemini")
    print(f"Model: {model_name}")
    print("Type 'exit', 'quit', or 'bye' to end the chat.")
    print("=" * 60)


def get_non_empty_input(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Please enter a message before sending.")


def print_ai_message(message: str) -> None:
    print(f"\nChatbot: {message}\n")


def print_error(message: str) -> None:
    print(f"\nError: {message}\n")
