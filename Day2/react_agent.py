"""Day 2 Assigned Task - ReAct agent."""

import json
import sys
from pathlib import Path

# Allow this file to use the existing Day 1 config.py
ROOT_PATH = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_PATH))

from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS


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


SYSTEM_PROMPT = """
You are a helpful assistant using a ReAct-style process.

You have access to the get_course_fee tool.

Rules:
1. Answer simple reasoning questions directly when no external information is needed.
2. For course-fee questions, use get_course_fee instead of guessing.
3. After receiving a tool result, use it to produce the final answer.
4. Do not invent information.
5. Give a concise final answer.
"""


def run_agent(question, max_steps=6):
    """Run the ReAct agent for one question."""

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        # No tool call means the model has produced the final answer.
        if not message.tool_calls:
            return message.content.strip()

        messages.append(message)

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(tool_name)

            if function is None:
                result = f"Unknown tool: {tool_name}"
            else:
                try:
                    result = function(**arguments)
                except Exception as error:
                    result = f"Tool error: {error}"

            print(
                f"step {step}: "
                f"{tool_name}({arguments}) -> {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": str(result)
                }
            )

    return "Stopped: maximum steps reached."


if __name__ == "__main__":

    print(
        f"\n=== REACT AGENT | provider: groq | model: {MODEL} ===\n"
    )

    for number, question in QUESTIONS:

        print("=" * 72)
        print(f"{number}: {question}\n")

        answer = run_agent(question)

        print("FINAL ANSWER:")
        print(answer)
        print()
        