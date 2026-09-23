"""Day 2 Assigned Task - Self-Consistency."""

import sys
from pathlib import Path
from collections import Counter

ROOT_PATH = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_PATH))

from config import client, MODEL


QUESTION = (
    "A student has Rs. 30,000. If the total course fee is "
    "Rs. 27,000, how much money will remain?"
)


COT_PROMPT = (
    "You are a helpful assistant. Solve the problem step by step. "
    "Show the important calculation steps and then give a clear final answer."
)


RUNS = 5
TEMPERATURE = 0.8


def get_answer():
    """Run the same CoT question once."""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": COT_PROMPT
            },
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        temperature=TEMPERATURE
    )

    return response.choices[0].message.content.strip()


def extract_final_answer(text):
    """Try to extract the final answer from the response."""

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    for line in reversed(lines):

        lower = line.lower()

        if "final answer" in lower:

            if ":" in line:
                return line.split(":", 1)[1].strip()

            return line

    return lines[-1] if lines else "(empty)"


if __name__ == "__main__":

    print(
        f"\n=== SELF-CONSISTENCY | provider: groq | model: {MODEL} ===\n"
    )

    print("QUESTION:")
    print(QUESTION)
    print()

    answers = []

    for run in range(1, RUNS + 1):

        response = get_answer()

        answer = extract_final_answer(response)

        print(f"Run {run}:")
        print(answer)
        print()

        answers.append(answer)

    counts = Counter(answers)

    majority_answer, majority_count = counts.most_common(1)[0]

    print("=" * 72)
    print(
        f"Majority answer ({majority_count} of {RUNS} runs): "
        f"{majority_answer}"
    )

    print("\nCorrect answer: Rs. 3,000")

    normalized = (
    majority_answer
    .replace(",", "")
    .replace("₹", "")
    .replace("Rs.", "")
    .replace("Rs", "")
    .strip()
)

if "3000" in normalized:
    print("Majority answer correct: YES")
else:
    print("Majority answer correct: NO")