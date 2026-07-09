from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from google import genai
from google.genai import types

from config import Settings


class GeminiChatbot:
    """Small wrapper around the Google Gen AI SDK with session memory."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.logger = logging.getLogger(self.__class__.__name__)
        self.client = genai.Client(api_key=settings.gemini_api_key)
        self.system_prompt = self._load_system_prompt(settings.system_prompt_file)
        self.history: list[dict[str, Any]] = []

    def send_message(self, message: str) -> str:
        """Send a user message to Gemini and return the model response."""
        cleaned_message = message.strip()
        if not cleaned_message:
            raise ValueError("Message cannot be empty.")

        contents = [*self.history, self._content("user", cleaned_message)]

        response = self.client.models.generate_content(
            model=self.settings.model_name,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                temperature=self.settings.temperature,
            ),
        )

        answer = (response.text or "").strip()
        if not answer:
            answer = "I received an empty response from the model."

        self.history.append(self._content("user", cleaned_message))
        self.history.append(self._content("model", answer))
        self._log_conversation(cleaned_message, answer)

        return answer

    def clear_history(self) -> None:
        """Clear in-memory conversation history for the current session."""
        self.history.clear()

    @staticmethod
    def _content(role: str, text: str) -> dict[str, Any]:
        return {"role": role, "parts": [{"text": text}]}

    @staticmethod
    def _load_system_prompt(path: Path) -> str:
        return path.read_text(encoding="utf-8").strip()

    def _log_conversation(self, user_message: str, ai_response: str) -> None:
        timestamp = datetime.now().isoformat(timespec="seconds")
        self.logger.info("[%s] USER: %s", timestamp, user_message)
        self.logger.info("[%s] AI: %s", timestamp, ai_response)
