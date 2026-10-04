from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
APP_NAME = "A.H AI Assistant"
APP_VERSION = "0.1.0"
