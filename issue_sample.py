def divide(x, y):
    if y == 0:
        raise ValueError(f"Cannot divide {x} by {y}: the divisor is zero.")

    result = x / y
    print(f"{x} ÷ {y} = {result}")
    return result

divide(10, 2)
divide(15, 3)
