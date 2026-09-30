"""Common configuration and private student academic data."""

import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


PROVIDER = os.getenv("PROVIDER", "ollama").strip().lower()

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "huggingface":
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. Use ollama, groq or huggingface."
    )


if not API_KEY:
    raise SystemExit(
        f"No API key found for PROVIDER={PROVIDER}. Check your .env file."
    )


client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


# Fictional private student record for this assignment.
STUDENT_RECORD = {
    "student_name": "Student A",
    "subjects": {
        "Python": {
            "attendance": 72,
            "assignment": "Submitted"
        },
        "DBMS": {
            "attendance": 81,
            "assignment": "Not Submitted"
        },
        "Mathematics": {
            "attendance": 68,
            "assignment": "Submitted"
        }
    }
}


QUESTIONS = [
    "What is my Python attendance?",
    "Did I submit my DBMS assignment?",
    "Which subject has the lowest attendance?",
    "Which subjects need attention based on my attendance and assignment status?"
]


def banner(system_name):
    print(
        f"\n=== {system_name} | provider: {PROVIDER} | model: {MODEL} ===\n"
    )