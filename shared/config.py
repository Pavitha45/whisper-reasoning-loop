import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

REASONING_MODE = os.getenv("REASONING_MODE", "local")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

ANTHROPIC_MODEL = os.getenv(
    "ANTHROPIC_MODEL",
    "claude-sonnet-4-6"
)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")