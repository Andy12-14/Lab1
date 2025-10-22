def add(*numbers):
    """Adds an unlimited number of parameters."""
    return sum(numbers)

def subtract(*numbers):
    """Subtracts all subsequent numbers from the first number."""
    if not numbers:
        raise ValueError("Subtraction requires at least one number.")
    
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result