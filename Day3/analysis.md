# Assigned Day 3 - From Prompt to Action

## 1. Scenario

For this task, I selected a college course fee calculation scenario.

The purpose is to compare how an LLM answers questions by itself and how its answer changes when a calculator tool is available.

The scenario contains three questions:

1. What is the fee for CS101 if the course fee is ₹12,000?
2. CS101 costs ₹12,000 and AI202 costs ₹18,000. What is the total fee after a 10% discount?
3. Three courses cost ₹12,000, ₹18,000 and ₹15,000. What is the total after a 25% scholarship?

The first question is simple and can be answered directly. The calculation questions can benefit from an external calculator tool.

---

## 2. What is an LLM?

An LLM (Large Language Model) is a model that understands and generates human-like text based on patterns learned from large amounts of training data.

An LLM can answer many general questions without using an external tool. However, it does not always have access to current information or an external calculator.

It can also make mistakes in factual or numerical questions. Sometimes it may give an answer that sounds confident even when the answer is incorrect.

In this experiment, the no-tool LLM was able to calculate the course fees correctly. However, for important numerical calculations, using a calculator tool can make the process more reliable.

---

## 3. What is an Agent?

An agent is a system where an LLM can decide what action is needed to complete a task and use external tools when required.

A plain chatbot mainly receives a prompt and generates an answer.

An agent can follow a process such as:

User question → LLM decision → Tool call → Tool result → Final answer

The main difference is that an agent can interact with external tools instead of depending only on its internal model knowledge.

In this project, the tool-enabled script demonstrates a simple agent-like tool-use process.

---

## 4. What is a Tool and Tool Call?

A tool is an external function that the LLM can use to perform a specific task.

In this project, the tool is a calculator function called `calculate()`.

Example:

```text
calculate((12000+18000)*0.9)
A tool call happens when the LLM decides that it needs to use the external tool.

The calculator returns the result:
Calculation result: 27000.0
The LLM then uses this result to produce the final answer.
5. Why is a Tool Schema Needed?

The tool schema tells the LLM what tool is available, what the tool does, and what input it expects.

In this project, the schema tells the model that:

The tool name is calculate.
The tool is used for mathematical calculations.
The tool requires an expression.
The expression must be provided as a string.

Example:
{
    "name": "calculate",
    "description": "Calculate a mathematical expression accurately.",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string"
            }
        },
        "required": ["expression"]
    }
}
6. Step-by-Step Tool Call Flow

The tool-enabled process works as follows:

Step 1 - User asks a question

The user asks a course fee calculation question.

Step 2 - Question is sent to the LLM

The LLM receives the question along with the available calculator tool.

Step 3 - LLM decides whether a tool is required

For a numerical calculation, the LLM can decide to call the calculator.

Step 4 - LLM creates a tool call

For example:
calculate((12000+18000)*0.9)
Step 5 - Calculator executes the expression

The calculator returns:

Calculation result: 27000.0
Step 6 - Tool result is sent back to the LLM

The result is added to the conversation so the LLM can use it.

Step 7 - LLM generates the final answer

The LLM explains the calculation and gives the final answer:

₹27,000
7. Why Should a Tool Return Plain Text on Failure?

A tool should return a simple text message when something goes wrong instead of directly raising an error to the user.

For example:

Calculation failed: invalid expression

This makes the result easier for the LLM to understand and handle.

It also prevents a tool failure from unnecessarily stopping the complete interaction.
8. Plain LLM vs LLM with One Tool
Aspect	Plain LLM Prompt	LLM with One Tool
Source of answer	Model's internal knowledge and reasoning	Model plus external calculator
Fetch/compute outside memory	No external tool is available	Yes, through the calculator
Reliability on factual/numeric questions	Can make calculation or factual mistakes	Calculator can improve numerical reliability
Transparency	Shows only the generated answer	Can show tool call and tool result
Speed/Cost	Usually simpler and faster	Extra tool call adds some processing
9. Observation from the Experiment

I tested the same three questions using two scripts.

No-tool run

The no_tool.py script sent the questions directly to the LLM.

The LLM answered all three questions without using an external calculator.

The answers were:

CS101 fee = ₹12,000
Two-course fee after 10% discount = ₹27,000
Three-course fee after 25% scholarship = ₹33,750
Tool-enabled run

The tool_enabled.py script provided the calculator tool to the LLM.

For Question 1, the LLM answered directly because no calculation was necessary.

For Question 2, the LLM correctly called the calculator:

Tool call:
calculate((12000+18000)*0.9)

The tool returned:

Calculation result: 27000.0

The LLM then used this result to give the final answer of ₹27,000.

For Question 3, the LLM answered directly without calling the calculator.

This shows that making a tool available does not mean the model will always use it. The model decides when to make the tool call.

10. Suitability of Plain Prompt and Tool Use

A plain LLM prompt can be sufficient for simple questions, explanations, and information that does not require external computation.

A tool becomes useful when the task requires reliable calculations or information that the model cannot reliably provide from its own knowledge.

In this experiment, the calculator tool provided a separate calculation step and made the calculation process more transparent because the tool call and result could be observed.

11. Conclusion

This experiment helped me understand the difference between a normal LLM prompt and an LLM that can use a tool.

A plain LLM generates an answer directly from its model knowledge and reasoning.

