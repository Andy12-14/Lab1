def add(*numbers):
    """Adds an unlimited number of parameters."""
    print("CRISTIANO_RONALDO")
    return sum(numbers)

def subtract(*numbers):
    """Subtracts all subsequent numbers from the first number."""
    if not numbers:
        raise ValueError("Subtraction requires at least one number.")
    
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result 


def multiply(*numbers):
    """multiply an unlimted number of parameters"""
    L=list(numbers)
    P=1
    for elt in L:
        P*=elt
    return P 

def divide(*numbers):
    """Divides the first number by all subsequent numbers."""
    if not numbers:
        raise ValueError("Division requires at least one number.")
    
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= num

    return result





