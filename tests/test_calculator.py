# tests/test_calculator.py
import builtins
import pytest
from src import calculator


def test_choice_to_symbol_known():
    assert calculator.choice_to_symbol('1') == '+'
    assert calculator.choice_to_symbol('2') == '-'
    assert calculator.choice_to_symbol('3') == '*'
    assert calculator.choice_to_symbol('4') == '/'


def test_choice_to_symbol_unknown():
    assert calculator.choice_to_symbol('9') == '?'


def test_get_input_number_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt='': '  3.5  ')
    val = calculator.get_input('Enter: ')
    assert isinstance(val, float)
    assert val == 3.5


def test_get_input_number_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(['abc', '4.2'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    val = calculator.get_input('Enter: ')
    captured = capsys.readouterr()
    assert 'Invalid input' in captured.out
    assert val == 4.2


def test_get_input_non_number(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt='': 'YES')
    val = calculator.get_input('Enter: ', is_number=False)
    assert val == 'yes'


def test_run_calculator_add_flow(monkeypatch, capsys):
    # Simulate the following inputs:
    # choice '1' (Add), num1 '2', num2 '3', another 'n'
    inputs = iter(['1', '2', '3', 'n'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))

    # Run the calculator (it will exit after 'n')
    calculator.run_calculator()
    out = capsys.readouterr().out
    assert 'Result' in out
    assert '2.0 + 3.0' in out
    assert 'Thank you for using the calculator' in out


def test_run_calculator_invalid_choice(monkeypatch, capsys):
    # Simulate invalid choice '9', then valid choice '1', numbers, and exit
    inputs = iter(['9', '1', '2', '3', 'n'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    calculator.run_calculator()
    out = capsys.readouterr().out
    assert 'Invalid choice' in out
    assert 'Result' in out


def test_run_calculator_divide_by_zero(monkeypatch, capsys):
    # Simulate divide by zero path: choice '4', num1 '10', num2 '0', exit
    inputs = iter(['4', '10', '0', 'n'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    calculator.run_calculator()
    out = capsys.readouterr().out
    assert 'Error:' in out
    assert 'Cannot divide by zero' in out


def test_run_calculator_unexpected_exception(monkeypatch, capsys):
    # Monkeypatch divide to raise an unexpected exception, ensure message printed
    def fake_div(a, b):
        raise RuntimeError('boom')

    # Replace divide used by calculator with fake_div
    monkeypatch.setattr(calculator, 'divide', fake_div)

    # Simulate inputs: choose '4', then numbers '2' and '3', then 'n'
    inputs = iter(['4', '2', '3', 'n'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))

    calculator.run_calculator()
    out = capsys.readouterr().out
    assert 'An unexpected error occurred' in out
