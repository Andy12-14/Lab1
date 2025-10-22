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


def multiply(*numbers):
    """multiply an unlimted number of parameters"""
    L=list(numbers)
    P=1
    for elt in L:
        P*=elt
    return P 

def divide(*numbers):
    """divide an unlimted number of parameters"""
    L=list(numbers)
    D=L[0]
    for elt in L[1:]:
        if elt==0:
            raise ZeroDivisionError("can not divide by zero")
        D/=elt
    return D 





