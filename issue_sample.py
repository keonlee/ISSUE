def divide(x, y):
    """Divide x by y and print the result.

    Raises:
        ValueError: If y is 0.
        TypeError: If x or y is not a number.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be numbers.")
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    result = x / y
    print(f"{x} ÷ {y} = {result}")
    return result


def main():
    divide(10, 2)
    divide(15, 3)


if __name__ == "__main__":
    main()