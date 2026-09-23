# Day 2 - Reasoning and Acting

This folder contains my Day 2 assigned task for the Agentic AI training.

## Topic

The task is about comparing:

- Direct Prompting
- Chain-of-Thought (CoT)
- ReAct Agent

It also includes a self-consistency experiment.

The aim is to understand how these approaches handle reasoning, tool usage, multi-step questions, and repeated answers.

## Scenario

For this task, I used a simple student course planning scenario.

The course fee data used by the tool is:

| Course | Fee |
|---|---:|
| CS101 | Rs. 12,000 |
| AI202 | Rs. 18,000 |
| DS303 | Rs. 15,000 |

The questions used in the experiment included simple reasoning questions and one question that needed course-fee information from a tool.

## Approaches Compared

### 1. Direct Prompting

Direct prompting asks the model for the answer directly without showing reasoning and without using tools.

In my experiment, it correctly answered the simple reasoning questions.

For the AI202 fee question, it could not provide the actual fee because it did not have access to the course-fee tool.

### 2. Chain-of-Thought

Chain-of-Thought asks the model to solve the question step by step before giving the final answer.

In my experiment, CoT correctly solved the reasoning questions and showed the calculation or logical steps.

However, it also could not answer the AI202 fee question because it did not have tool access.

### 3. ReAct Agent

The ReAct agent can combine reasoning with tool actions and observations.

For simple reasoning questions, it answered directly.

For the AI202 fee question, it called:

```text
get_course_fee({'course_code': 'AI202'})
Self-Consistency

The self-consistency experiment runs the same reasoning question multiple times with a non-zero temperature and compares the final answers.

In this task:

RUNS = 5
TEMPERATURE = 0.8

The five runs gave different wording but the same numerical answer for the question:

Rs. 3,000

The experiment was also repeated with temperature set to 0 to observe the change in consistency.
My Observation

From the experiments, I observed that:

Direct Prompting
→ Gives the answer directly

Chain-of-Thought
→ Gives step-by-step reasoning

ReAct
→ Uses reasoning and tools when external information is needed

Self-Consistency
→ Runs the same reasoning problem multiple times and compares answers

Direct Prompting and CoT could solve questions when all the required information was already available in the question.

ReAct was able to get the AI202 fee because it could use the course-fee tool.
This task helped me understand the difference between direct prompting, Chain-of-Thought, and ReAct.

Direct prompting is useful for simple questions.

Chain-of-Thought is useful when a problem needs step-by-step reasoning.

ReAct is useful when the problem needs external information or tools.

Self-consistency can be used by running the same reasoning problem multiple times and comparing the final answers.

The detailed comparison and observations are given in analysis.md.