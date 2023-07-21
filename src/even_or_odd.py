def even_or_odd(number):
    if number != int(number):
        raise ValueError("Number must be an integer")
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
