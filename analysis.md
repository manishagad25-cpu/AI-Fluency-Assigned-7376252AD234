# Day 1 Assigned Task - Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario Chosen

For this task, I chose a small student academic tracker scenario using fictional private data. The record contains attendance and assignment information for three subjects: Python, DBMS, and Mathematics.

The private record used in the project is:

- Python – 72% attendance, Assignment Submitted
- DBMS – 81% attendance, Assignment Not Submitted
- Mathematics – 68% attendance, Assignment Submitted

For this project, I used 75% attendance as the simple threshold for identifying a subject that needs attention. This threshold is only a rule used in this project.

The same four questions were tested in the three systems:

1. What is my Python attendance?
2. Did I submit my DBMS assignment?
3. Which subject has the lowest attendance?
4. Which subjects need attention based on my attendance and assignment status?

The purpose was to see how the same private-data problem behaves when it is handled by a plain chatbot, a fixed rule-based workflow, and an AI agent.

## 2. Plain Chatbot

The plain chatbot uses the LLM to generate responses, but it does not have access to the private student record. The private academic data is kept outside the chatbot code.

When I asked, “What is my Python attendance?”, the chatbot said that it did not have access to my personal academic records. It gave the same type of response for the DBMS assignment question, the lowest attendance question, and the question about which subjects need attention.

This shows a limitation of a plain chatbot in this scenario. The LLM can understand the question and produce a natural-language response, but it cannot reliably answer questions about private academic information when that information is not connected to it. In my run, the chatbot did not invent an attendance value or assignment status.

The main advantage of the chatbot is simple natural-language conversation. It is useful for general questions and explanations that do not require access to private records. Its limitation in this scenario is that it cannot retrieve the student's private academic data.

## 3. Rule-Based Workflow

The rule-based workflow uses predefined Python conditions and directly reads the private student record. No LLM call is used in this system.

The workflow checks the question and applies a matching rule. For the Python attendance question, it reads the Python attendance and returns 72%. For the DBMS assignment question, it reads the assignment status and returns “Not Submitted”. For the lowest attendance question, it compares the attendance values and identifies Mathematics at 68%. For the final question, it checks attendance and assignment status for all three subjects.

My actual workflow results were:

- Python attendance was 72%.
- DBMS assignment status was Not Submitted.
- Mathematics had the lowest attendance at 68%.
- Python, DBMS, and Mathematics were identified as subjects needing attention under the 75% attendance rule and assignment-status rule used in this project.

The workflow is predictable because the rules are written by the programmer. For the questions covered by the rules, the answers are consistent. However, the workflow is rigid. A new question that is not covered by the predefined conditions may not be handled properly unless a new rule is added.

## 4. AI Agent

The AI agent combines an LLM, tools, and a loop. In this project, the agent does not guess the private information. Instead, it can use the tools `get_attendance`, `get_assignment_status`, and `calculator`.

For the Python attendance question, the agent called `get_attendance` for Python and returned 72%. For the DBMS assignment question, it called `get_assignment_status` for DBMS and returned that the assignment had not been submitted.

For the lowest attendance question, the agent checked the attendance of Python, DBMS, and Mathematics. It then identified Mathematics as the subject with the lowest attendance at 68%.

The last question showed the multi-step nature of the agent. It first checked the attendance of all three subjects and then checked the assignment status of all three subjects. After receiving those results, it produced a final answer identifying Python, DBMS, and Mathematics as needing attention. In the successful run, six tool steps were used before the final answer.

During an earlier run, the agent reached the maximum step limit before producing a final answer for the last question. I increased the allowed steps from 6 to 8, and the task then completed successfully. This showed that an agent can handle multi-step tasks flexibly, but the execution also depends on the loop limit and the way the LLM chooses its actions.

## 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High for general conversation, but limited for private academic questions without connected data | Low to medium because it depends on predefined rules | High because the LLM can choose among available tools |
| Decision-making | Generates a response from the LLM but has no private-data lookup in this project | Decisions come from fixed conditions written in the program | The LLM decides what information or tool is needed and can continue through multiple steps |
| Tool usage | No tools | No tools; uses direct program logic and stored data | Uses `get_attendance`, `get_assignment_status`, and `calculator` |
| Private-data access | No access to the student record | Direct access to the private student record | Accesses the private record through tools |
| Multi-step task handling | Limited for this scenario because the required private data is unavailable | Possible only when the required steps are explicitly programmed | Stronger for multi-step questions because the agent can call several tools and then combine the results |
| Automation | Simple question-and-answer interaction | Good for fixed and repeatable tasks | Good for tasks that need tool selection and multiple actions |
| Reliability | Did not invent private data in my run, but could not answer the private-data questions | Predictable for the rules that were programmed | Produced the required answers after the step limit was increased, but execution can depend on tool calls and loop limits |

## 6. Suitability Analysis

For this student academic tracker, the rule-based workflow is suitable for routine questions with fixed definitions and fixed data, such as checking a subject attendance percentage or checking whether an assignment is submitted. Its main advantage is predictable behaviour because the conditions are explicitly programmed.

The AI agent is more suitable when the student asks a question that needs several pieces of private information to be collected and combined. In this project, the question about subjects needing attention required multiple attendance and assignment lookups before a final response could be produced. The agent handled this by selecting tools and continuing through the loop.

The plain chatbot is useful for general student assistance, but it is not suitable by itself for this private-data scenario because the chatbot had no access to the academic record in my implementation. It therefore could not provide the requested attendance or assignment information.

For the overall scenario, the AI agent is the most suitable of the three when the system needs to handle both simple private-data questions and more flexible multi-step requests. The workflow is still useful for fixed, predictable operations, while the chatbot is useful for general conversation that does not require private records.

## 7. Conclusion

This task showed the practical difference between a plain chatbot, a rule-based workflow, and an AI agent.

A plain chatbot mainly uses an LLM to understand a user's question and generate a response. It is useful for general conversation, explanations, and questions that do not depend on private records or controlled business logic.

A rule-based workflow follows predefined conditions and steps. It does not need an LLM and is useful when the problem is well defined and the expected result should be predictable and repeatable. In my academic tracker, it correctly answered the predefined questions because the rules directly matched the stored data.

An AI agent combines an LLM, tools, and a loop. It can decide which tool to use, observe the tool result, and continue with another action before giving the final response. In my project, the agent accessed the private academic information through tools and handled the multi-step question about subjects needing attention.

In general, a chatbot is appropriate for simple conversational assistance, a rule-based workflow is appropriate for fixed and predictable tasks, and an AI agent is appropriate when a task needs flexible decision-making, tool usage, and multiple steps.
