"""System 2: Rule-based workflow using fixed conditions."""

from config import STUDENT_RECORD, QUESTIONS


def workflow(question):
    q = question.lower()
    subjects = STUDENT_RECORD["subjects"]

    # Rule 1: Python attendance
    if "python" in q and "attendance" in q:
        attendance = subjects["Python"]["attendance"]
        return f"Python attendance is {attendance}%."

    # Rule 2: DBMS assignment status
    if "dbms" in q and "assignment" in q:
        status = subjects["DBMS"]["assignment"]
        return f"DBMS assignment status: {status}."

    # Rule 3: Find the subject with the lowest attendance
    if "lowest attendance" in q:
        lowest_subject = min(
            subjects,
            key=lambda subject: subjects[subject]["attendance"]
        )
        lowest_attendance = subjects[lowest_subject]["attendance"]
        return (
            f"{lowest_subject} has the lowest attendance "
            f"at {lowest_attendance}%."
        )

    # Rule 4: Find subjects that need attention
    if "need attention" in q:
        needs_attention = []

        for subject, data in subjects.items():
            if data["attendance"] < 75 or data["assignment"] == "Not Submitted":
                needs_attention.append(
                    f"{subject} ({data['attendance']}%, {data['assignment']})"
                )

        if needs_attention:
            return "Subjects needing attention: " + ", ".join(needs_attention)

        return "No subjects currently need attention."

    return "I can answer only the predefined academic questions."


if __name__ == "__main__":
    print("\n=== RULE-BASED WORKFLOW ===\n")

    for i, question in enumerate(QUESTIONS, start=1):
        print(f"Q{i}: {question}")
        print("A :", workflow(question))
        print()