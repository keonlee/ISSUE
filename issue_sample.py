def _display_result(x, operator, y, result):
    print(f"{x} {operator} {y} = {result}")
    return result


def add(x, y):
    return _display_result(x, "+", y, x + y)


def subtract(x, y):
    return _display_result(x, "-", y, x - y)


def multiply(x, y):
    return _display_result(x, "×", y, x * y)


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")

    return _display_result(x, "÷", y, x / y)


def power(x, y):
    return _display_result(x, "**", y, x**y)


def modulo(x, y):
    return _display_result(x, "%", y, x % y)


_OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "modulo": modulo,
}


def calculate(operation, x, y):
    try:
        calculation = _OPERATIONS[operation]
    except KeyError:
        raise ValueError(f"Unsupported operation: {operation}") from None
    return calculation(x, y)


if __name__ == "__main__":
    divide(10, 2)
    divide(15, 3)
