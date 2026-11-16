def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")

    result = x / y
    print(f"{x} ÷ {y} = {result}")
    return result


def main():
    x = get_number("Enter the dividend: ")
    y = get_number("Enter the divisor: ")
    divide(x, y)


if __name__ == "__main__":
    main()
