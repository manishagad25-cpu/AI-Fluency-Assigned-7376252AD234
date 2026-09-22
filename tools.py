"""Tools available to the AI agent."""

import ast
import operator

from config import STUDENT_RECORD


def get_attendance(subject: str) -> str:
    """Get the attendance percentage for a subject."""

    subjects = STUDENT_RECORD["subjects"]

    # Match subject names without worrying about uppercase/lowercase.
    subject_lookup = {
        name.lower(): name
        for name in subjects
    }

    subject_name = subject_lookup.get(subject.strip().lower())

    if subject_name is None:
        return f"Unknown subject: {subject}"

    attendance = subjects[subject_name]["attendance"]

    return f"{subject_name} attendance is {attendance}%."


def get_assignment_status(subject: str) -> str:
    """Get the assignment submission status for a subject."""

    subjects = STUDENT_RECORD["subjects"]

    # Match subject names without worrying about uppercase/lowercase.
    subject_lookup = {
        name.lower(): name
        for name in subjects
    }

    subject_name = subject_lookup.get(subject.strip().lower())

    if subject_name is None:
        return f"Unknown subject: {subject}"

    status = subjects[subject_name]["assignment"]

    return f"{subject_name} assignment status: {status}."


# Basic arithmetic operations allowed by the calculator.
_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def _evaluate(node):
    """Safely evaluate a basic arithmetic expression."""

    if isinstance(node, ast.Constant) and isinstance(
        node.value, (int, float)
    ):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""

    try:
        result = _evaluate(
            ast.parse(expression, mode="eval").body
        )
        return str(result)

    except Exception as error:
        return f"Calculator error: {error}"


# Maps tool names to actual Python functions.
TOOL_FUNCTIONS = {
    "get_attendance": get_attendance,
    "get_assignment_status": get_assignment_status,
    "calculator": calculator,
}


# Tool descriptions given to the LLM.
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_attendance",
            "description": (
                "Get the private attendance percentage "
                "for one subject."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {
                        "type": "string"
                    }
                },
                "required": ["subject"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_assignment_status",
            "description": (
                "Get the private assignment submission status "
                "for one subject."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {
                        "type": "string"
                    }
                },
                "required": ["subject"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Calculate a basic arithmetic expression "
                "using +, -, and *."
            ),
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
    }
]


# Test the tools directly when this file is run.
if __name__ == "__main__":
    print(
        "Attendance:",
        get_attendance("Python")
    )

    print(
        "Assignment:",
        get_assignment_status("DBMS")
    )

    print(
        "Calculator:",
        calculator("72 - 68")
    )