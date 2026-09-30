def calculate(expression):
    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except Exception as e:
        return f"Calculation failed: {e}"


if __name__ == "__main__":
    print(calculate("12000 + 18000"))