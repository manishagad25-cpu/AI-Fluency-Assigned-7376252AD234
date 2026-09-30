from openai import OpenAI
from config import client, MODEL


questions = [
    "What is the fee for CS101 if the course fee is ₹12,000?",
    "CS101 costs ₹12,000 and AI202 costs ₹18,000. What is the total fee after a 10% discount?",
    "Three courses cost ₹12,000, ₹18,000 and ₹15,000. What is the total after a 25% scholarship?"
]


def ask_llm(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        print("LLM Answer:", ask_llm(question))