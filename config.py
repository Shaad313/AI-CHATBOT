from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str
    model_name: str
    temperature: float
    log_file: Path
    system_prompt_file: Path


def load_settings() -> Settings:
    """Load application settings from environment variables and defaults."""
    load_dotenv(BASE_DIR / ".env")

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Copy .env.example to .env and add your Gemini API key."
        )
    if api_key == "replace_with_your_actual_gemini_api_key" or len(api_key) < 30:
        raise RuntimeError(
            "GEMINI_API_KEY is missing or too short. "
            "Create a Gemini API key at https://aistudio.google.com/app/apikey and paste the full key into .env."
        )

    model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash").strip()
    temperature = float(os.getenv("GEMINI_TEMPERATURE", "0.7"))
    log_file = BASE_DIR / "logs" / "chatbot.log"
    system_prompt_file = BASE_DIR / "prompts" / "system_prompt.txt"

    return Settings(
        gemini_api_key=api_key,
        model_name=model_name,
        temperature=temperature,
        log_file=log_file,
        system_prompt_file=system_prompt_file,
    )


def setup_logging(log_file: Path) -> None:
    """Configure file logging for conversations and errors."""
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
