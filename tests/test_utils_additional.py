# tests/test_utils_additional.py
import pytest
import math
from src.utils import add, subtract, multiply, divide


def test_add_no_args_returns_zero_and_type():
    # already covered, but assert type
    assert add() == 0
    assert isinstance(add(), int) or isinstance(add(), float)


def test_add_large_numbers():
    assert add(10**12, 10**12) == 2 * 10**12


def test_subtract_single_and_many():
    assert subtract(42) == 42
    assert subtract(100, 50, 25, 25) == 0


def test_subtract_with_negative_results():
    assert subtract(5, 10) == -5


def test_multiply_no_args_returns_one():
    assert multiply() == 1


def test_multiply_with_floats_precision():
    assert math.isclose(multiply(1.1, 2.0), 2.2, rel_tol=1e-9)


def test_divide_chain_and_precision():
    assert divide(10, 4) == 2.5
    assert math.isclose(divide(9, 2), 4.5, rel_tol=1e-9)


def test_divide_zero_in_middle_raises():
    with pytest.raises(ZeroDivisionError):
        divide(100, 2, 0, 5)


def test_divide_type_errors():
    # Passing a non-number for add/divide should raise TypeError when operations occur
    with pytest.raises(TypeError):
        add(1, 'a')

    # multiply with a string will repeat the string (Python semantics), so we assert that behavior
    assert multiply(2, 'b') == 'bb'

    with pytest.raises(TypeError):
        divide(10, 'c')
