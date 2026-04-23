def divide(x, y):
    if y == 0:
        print(f"Error: Cannot divide {x} by zero")
        return None

    result = x / y
    print(f"{x} ÷ {y} = {result}")
    return result

divide(10, 2)
divide(15, 3)