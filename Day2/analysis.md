# Day 2 Assigned Task - Reasoning and Acting

## 1. Scenario Chosen

For this task, I used a simple student course planning scenario. The scenario has some questions that can be solved using only the information given in the question and one question that needs external/private information.

The course fee data used by the tool is:

- CS101 - Rs. 12,000
- AI202 - Rs. 18,000
- DS303 - Rs. 15,000

The questions used in the experiments were:

1. A student has Rs. 30,000. If the total course fee is Rs. 27,000, how much money will remain?
2. A student studies for 2 hours on Monday, 3 hours on Tuesday, and 4 hours on Wednesday. What is the total study time?
3. Ravi scored more than Kumar. Kumar scored more than Arun. Who scored the lowest?
4. What is the fee for AI202?

The first three questions only need reasoning. The fourth question needs the course fee data from the tool.

## 2. Direct Prompting

Direct prompting gives the question directly to the model and asks for the final answer without visible reasoning.

In my experiment, the first three questions were answered correctly. The answers were Rs. 3,000, 9 hours, and Arun respectively.

For the AI202 fee question, the model said that it did not have the required information. This is because direct prompting did not have access to the course fee tool.

So, direct prompting is simple and fast, but it cannot fetch information that is not already available to the model.

## 3. Chain-of-Thought

Chain-of-Thought prompting asks the model to solve the question step by step before giving the final answer.

In my experiment, the first three questions were answered correctly with CoT. The responses were longer because the model showed the calculation or reasoning steps.

For example, for the first question, the model showed the subtraction:

30,000 - 27,000 = 3,000

For the AI202 fee question, CoT still could not give the actual fee because it had no tool access. This shows that step-by-step reasoning does not give the model new external information.

## 4. ReAct Agent

The ReAct agent works by using reasoning together with actions and observations.

The basic flow is:

Question
→ Decide what information is needed
→ Action: call a tool
→ Observation: receive the tool result
→ Final answer

In my experiment, the first three questions were answered directly because all the required information was already present in the questions.

For the AI202 fee question, the agent called:

get_course_fee({'course_code': 'AI202'})

The tool returned:

AI202 fee is Rs. 18000.

The agent then used this result and gave the final answer:

The fee for AI202 is Rs. 18,000.

This shows the main advantage of ReAct in this scenario. It can get information from a tool when the model does not already have the required fact.

## 5. Comparison Table

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Low, gives the answer directly | Higher because the problem is solved step by step | Higher because it can reason and take actions |
| Tool usage | No tools | No tools | Uses the course-fee tool when required |
| Reliability on multi-step questions | Works for simple questions, but no tool support | Better for multi-step reasoning | Can handle reasoning plus external information |
| Transparency | No visible reasoning | Shows the reasoning steps | Shows tool actions and observations |
| Speed / cost | Fastest and lowest because it uses one direct response | Slower and longer because more text is generated | Can take more time because it may need tool calls and more model steps |
| Consistency across repeated runs | Depends on the model and temperature | Can vary when temperature is non-zero | Depends on tool calls and model decisions |

## 6. Self-Consistency Observation

I used the first reasoning question for the self-consistency experiment.

The program was run 5 times with:

RUNS = 5  
TEMPERATURE = 0.8

The five outputs used different wording, but all of them gave the same numerical answer:

Rs. 3,000

The program reported a majority answer based on the exact extracted text. Because the wording and formatting were different, the printed majority count was lower even though the numerical answer was the same.

This shows that self-consistency can produce different response wording while still reaching the same answer.

For the temperature 0 test, the responses became much more consistent compared with the non-zero temperature run. At temperature 0, there is much less variation between repeated outputs.

## 7. Suitability Analysis

For this scenario, direct prompting is useful for simple questions where all the required information is already given. It is fast and easy to use.

Chain-of-Thought is useful when a question needs several reasoning or calculation steps. In my experiment, it gave clear step-by-step solutions for the first three questions.

ReAct is useful when the question needs information from outside the model. In my experiment, the AI202 fee question could not be answered by direct prompting or CoT, but the ReAct agent used the tool and got the correct fee.

Therefore, the suitable approach depends on the type of question. Simple questions can use direct prompting, reasoning questions can use CoT, and questions that need external information or tools can use ReAct.

## 8. Conclusion

This task helped me understand the difference between Direct Prompting, Chain-of-Thought, and ReAct.

Direct prompting gives an answer directly from the model without visible reasoning or tools.

Chain-of-Thought asks the model to solve the problem step by step. It can help with multi-step reasoning, but it cannot provide a fact that is not available to the model.

ReAct combines reasoning with actions and observations. It can call a tool, get the required information, and then use that result to answer the question.

I also understood self-consistency, where the same reasoning question is run multiple times and the answers are compared. The temperature affects how much the outputs vary across repeated runs.

Overall, the main difference I learned is:

Direct Prompting = Direct answer

Chain-of-Thought = Step-by-step reasoning

ReAct = Reasoning + Tool action + Observation