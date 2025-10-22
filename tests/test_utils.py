# tests/test_utils.py
import pytest
from src.utils import add, subtract, multiply, divide

# Partner A's tests
def test_add_normal_cases():
    assert add(1, 2, 3) == 6
    assert add(10, 5) == 15
    assert add(-1, 1, 0) == 0

def test_add_edge_cases():
    assert add(5) == 5
    assert add() == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract_normal_cases():
    assert subtract(10, 2, 1) == 7  # 10 - 2 - 1
    assert subtract(50, 25) == 25

def test_subtract_edge_cases():
    assert subtract(10) == 10
    with pytest.raises(ValueError):
        subtract()
    assert subtract(10, 5, -2) == 7 # 10 - 5 - (-2) = 7

# Partner B's tests
def test_multiply_normal_cases():
    assert multiply(2, 3, 4) == 24
    assert multiply(5, 0) == 0
    assert multiply(-2, 3) == -6

def test_multiply_edge_cases():
    assert multiply(7) == 7
    assert multiply() == 1 # 1 is the typical result for an empty product
    assert multiply(1.5, 2) == 3.0

def test_divide_normal_cases():
    assert divide(10, 2, 5) == 1  # 10 / 2 / 5
    assert divide(100, 10) == 10.0

def test_divide_edge_cases():
    assert divide(5) == 5.0
    with pytest.raises(ValueError):
        divide()

def test_divide_by_zero_case():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    with pytest.raises(ZeroDivisionError):
        divide(100, 2, 0, 5)

