"""System 3: AI agent using an LLM, tools, and a loop."""

import json

from config import client, MODEL, QUESTIONS
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a student academic assistant.

You can access private academic data only through the provided tools.

Available subjects:
- Python
- DBMS
- Mathematics

Rules:
1. Never guess private attendance or assignment information.
2. Use get_attendance to check attendance.
3. Use get_assignment_status to check assignment status.
4. Use calculator when arithmetic is needed.
5. For questions about the lowest attendance, check the attendance
   of all relevant subjects before answering.
6. For questions about subjects needing attention, check the attendance
   and assignment status of all relevant subjects.
7. After receiving tool results, give a clear final answer.
8. If no tool is needed, answer directly.
"""


def agent(question, max_steps=8, verbose=True):
    """
    Run the AI agent.

    The loop allows the LLM to:
    1. Decide what to do.
    2. Call one or more tools.
    3. Observe the tool results.
    4. Continue until a final answer is produced.
    """

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

        # If the LLM has no more tools to call,
        # it has produced the final answer.
        if not message.tool_calls:
            return message.content.strip()

        # Add the assistant's tool-call message to the conversation.
        messages.append(message)

        # Execute every tool selected by the LLM.
        for call in message.tool_calls:

            tool_name = call.function.name

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(tool_name)

            if function is None:
                result = f"Unknown tool: {tool_name}"
            else:
                try:
                    result = function(**arguments)
                except Exception as error:
                    result = f"Tool error: {error}"

            if verbose:
                print(
                    f" step {step}: "
                    f"{tool_name}({arguments}) -> {result}"
                )

            # Send the tool result back to the LLM.
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "name": tool_name,
                    "content": str(result)
                }
            )

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":

    print("\n=== AI AGENT | LLM + TOOLS + LOOP ===\n")

    for question in QUESTIONS:
        print("Q:", question)

        answer = agent(question)

        print("A:", answer)
        print("-" * 70)