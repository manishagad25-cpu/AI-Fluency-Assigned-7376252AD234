"""System 1: Plain chatbot using only an LLM."""

from config import client, MODEL


SYSTEM_PROMPT = (
    "You are a general student assistant. "
    "You do not have access to any private student academic records. "
    "Do not invent attendance percentages or assignment status. "
    "For questions about private academic data, clearly say that the data "
    "is not available to you."
)


print(f"\n=== PLAIN CHATBOT | model: {MODEL} ===\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        break

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    print("Bot:", response.choices[0].message.content.strip())
    print()