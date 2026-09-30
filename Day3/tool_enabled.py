import json
from config import client, MODEL
from calculator_tool import calculate


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression accurately.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


questions = [
    "What is the fee for CS101 if the course fee is ₹12,000?",
    "CS101 costs ₹12,000 and AI202 costs ₹18,000. What is the total fee after a 10% discount?",
    "Three courses cost ₹12,000, ₹18,000 and ₹15,000. What is the total after a 25% scholarship?"
]


def ask_llm(question):
    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            if tool_call.function.name == "calculate":
                arguments = json.loads(tool_call.function.arguments)
                expression = arguments["expression"]

                print("Tool call:")
                print(f"  calculate({expression})")

                tool_result = calculate(expression)

                print("Tool result:")
                print(f"  {tool_result}")

                messages.append(message)
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result
                    }
                )

        final_response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        return final_response.choices[0].message.content

    return message.content


if __name__ == "__main__":
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        print("Final Answer:", ask_llm(question))