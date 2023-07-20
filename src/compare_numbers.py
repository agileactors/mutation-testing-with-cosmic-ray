def compare_numbers(a, b):
    if a == b:
        return f"{a} is greater than {b}"
    elif a is not b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"