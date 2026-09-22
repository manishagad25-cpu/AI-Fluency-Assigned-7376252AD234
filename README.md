# AI Fluency Training – Day 1 Assigned Task

## Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

This repository contains my Day 1 assigned task for the Agentic AI training.

The task compares three approaches using the same private-data scenario:

- Plain Chatbot
- Rule-Based Workflow
- AI Agent

## Scenario

I used a small fictional student academic tracker containing attendance and assignment information for three subjects.

| Subject | Attendance | Assignment |
|---|---:|---|
| Python | 72% | Submitted |
| DBMS | 81% | Not Submitted |
| Mathematics | 68% | Submitted |

For this project, attendance below 75% is treated as needing attention.

## Questions Tested

The same questions were tested using the three approaches:

1. What is my Python attendance?
2. Did I submit my DBMS assignment?
3. Which subject has the lowest attendance?
4. Which subjects need attention based on my attendance and assignment status?

## Plain Chatbot

The plain chatbot uses the LLM without access to the private student record.

In my run, it could understand the questions but said that it could not access the student's private academic information.

## Rule-Based Workflow

The rule-based workflow uses predefined Python conditions and directly accesses the stored student data.

It does not use an LLM. It gives predictable answers for the questions covered by the programmed rules.

## AI Agent

The AI agent combines:

```text
LLM + Tools + Loop
The agent can use these tools:

get_attendance
get_assignment_status
calculator

It selects the required tools, receives their results, and continues through the loop before giving the final answer.
Project Structure

AI-Fluency-Assigned-7376252AD234
├── .gitignore
├── agent.py
├── analysis.md
├── chatbot.py
├── config.py
├── requirements.txt
├── tools.py
├── workflow.py
└── Output
    ├── agent1.png
    ├── chatbot1.png
    └── workflow1.png

    Files
chatbot.py

Plain LLM-based chatbot without access to the private student record.

workflow.py

Rule-based implementation using predefined conditions and the private student data.

tools.py

Contains the tools used by the AI agent.

agent.py

Implements the AI agent using an LLM, tools, and a loop.

config.py

Contains the LLM configuration and the fictional academic data used in the experiment.

analysis.md

Contains the detailed comparison, suitability analysis, and conclusion for the task.

Output/

Contains screenshots of the three systems running.