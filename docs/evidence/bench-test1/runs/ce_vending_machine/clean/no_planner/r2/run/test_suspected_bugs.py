# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import VendingMachine
def test_display_multiple_items():
    vm = VendingMachine()
    vm.inventory = {
        'Coke': {'price': 1.25, 'quantity': 10},
        'Pepsi': {'price': 1.50, 'quantity': 5}
    }
    result = vm.display_items()
    lines = result.split('\n')
    assert len(lines) == 2
    assert 'Coke - $1.25 [10]' in lines
    assert 'Pepsi - $1.50 [5]' in lines

from solution import VendingMachine

def test_display_price_two_decimals():
    vm = VendingMachine()
    vm.inventory = {'Coke': {'price': 1.5, 'quantity': 10}}
    result = vm.display_items()
    # The reviewer fix requires :.2f formatting, so 1.5 must become $1.50
    assert result == 'Coke - $1.50 [10]', f'Got: {result!r}'

from solution import VendingMachine

def test_display_multiple_items():
    vm = VendingMachine()
    vm.inventory = {
        'Coke': {'price': 1.50, 'quantity': 10},
        'Pepsi': {'price': 2.00, 'quantity': 5}
    }
    result = vm.display_items()
    lines = result.split('\n')
    assert len(lines) == 2
    assert 'Coke - $1.50 [10]' in result
    assert 'Pepsi - $2.00 [5]' in result

from solution import VendingMachine

def test_display_integer_price():
    vm = VendingMachine()
    vm.inventory = {'Water': {'price': 2.0, 'quantity': 3}}
    result = vm.display_items()
    # With :.2f, 2.0 becomes $2.00; without it would be $2.0
    assert result == 'Water - $2.00 [3]', f'Got: {result!r}'

from solution import VendingMachine

def test_display_three_items():
    vm = VendingMachine()
    vm.inventory = {
        'A': {'price': 0.5, 'quantity': 1},
        'B': {'price': 1.0, 'quantity': 2},
        'C': {'price': 3.14, 'quantity': 3}
    }
    result = vm.display_items()
    assert 'A - $0.50 [1]' in result
    assert 'B - $1.00 [2]' in result
    assert 'C - $3.14 [3]' in result
    assert result.count('\n') == 2
