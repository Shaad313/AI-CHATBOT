from __future__ import annotations

from pathlib import Path

from chatbot import GeminiChatbot
from config import Settings


def test_content_format() -> None:
    content = GeminiChatbot._content("user", "Hello")

    assert content == {"role": "user", "parts": [{"text": "Hello"}]}


def test_load_system_prompt(tmp_path: Path) -> None:
    prompt_file = tmp_path / "system_prompt.txt"
    prompt_file.write_text(" Be helpful. \n", encoding="utf-8")

    assert GeminiChatbot._load_system_prompt(prompt_file) == "Be helpful."


def test_settings_shape() -> None:
    settings = Settings(
        gemini_api_key="test-key",
        model_name="gemini-2.0-flash",
        temperature=0.7,
        log_file=Path("logs/chatbot.log"),
        system_prompt_file=Path("prompts/system_prompt.txt"),
    )

    assert settings.gemini_api_key == "test-key"
    assert settings.model_name.startswith("gemini")
