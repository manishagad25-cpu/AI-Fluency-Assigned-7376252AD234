"""Compare Direct Prompting and Chain-of-Thought on the same questions."""

import sys
from pathlib import Path

# Allow Day 2 to reuse the existing Day 1 config.py.
DAY1_PATH = Path(__file__).resolve().parent.parent

sys.path.append(str(DAY1_PATH))

from config import client, MODEL


QUESTIONS = [
    (
        "Q1",
        "A student has Rs. 30,000. If the total course fee is "
        "Rs. 27,000, how much money will remain?"
    ),
    (
        "Q2",
        "A student studies for 2 hours on Monday, 3 hours on Tuesday, "
        "and 4 hours on Wednesday. What is the total study time?"
    ),
    (
        "Q3",
        "Ravi scored more than Kumar. Kumar scored more than Arun. "
        "Who scored the lowest?"
    ),
    (
        "Q4",
        "What is the fee for AI202?"
    ),
]


DIRECT_PROMPT = (
    "You are a helpful assistant. Give only the final answer. "
    "Do not explain your reasoning. "
    "You do not have access to external tools or private databases."
)


COT_PROMPT = (
    "You are a helpful assistant. Solve the question step by step. "
    "Show the important reasoning or calculation steps, then give a "
    "clear final answer. You do not have access to external tools or "
    "private databases."
)


def ask(system_prompt, question):
    """Send one question to the model."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print(
        f"\n=== DIRECT vs CoT | provider: groq | model: {MODEL} ===\n"
    )

    for number, question in QUESTIONS:

        print("=" * 72)
        print(f"{number}: {question}\n")

        print("--- DIRECT PROMPTING ---")
        direct_answer = ask(
            DIRECT_PROMPT,
            question
        )
        print(direct_answer)
        print()

        print("--- CHAIN-OF-THOUGHT ---")
        cot_answer = ask(
            COT_PROMPT,
            question
        )
        print(cot_answer)
        print()