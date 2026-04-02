def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    result = x / y
    print(f"{x} ÷ {y} = {result}")
    return result


if __name__ == "__main__":
    divide(10, 2)
    divide(15, 3)

    