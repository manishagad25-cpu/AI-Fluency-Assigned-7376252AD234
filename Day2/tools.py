"""Tools used by the Day 2 ReAct agent."""

COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


def get_course_fee(course_code: str) -> str:
    """Return the fee for a course."""
    code = course_code.strip().upper()

    fee = COURSE_FEES.get(code)

    if fee is None:
        return f"Unknown course code: {course_code}"

    return f"{code} fee is Rs. {fee}."


TOOL_FUNCTIONS = {
    "get_course_fee": get_course_fee
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee for a course code such as CS101, AI202, or DS303.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string"
                    }
                },
                "required": ["course_code"]
            }
        }
    }
]


if __name__ == "__main__":
    print(get_course_fee("AI202"))