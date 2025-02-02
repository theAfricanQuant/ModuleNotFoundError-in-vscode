def sum_numbers(*args):
    """Sum any number of input values."""
    return sum(args)

def multiply_numbers(*args):
    """Multiply any number of input values."""
    result = 1
    for num in args:
        result *= num
    return result