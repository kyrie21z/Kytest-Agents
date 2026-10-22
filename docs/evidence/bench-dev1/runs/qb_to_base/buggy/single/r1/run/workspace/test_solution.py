# Accepted by submit_tests; explanations in testgen_report.json.

def test_to_base_single_digit():
    from solution import to_base
    result = to_base(5, 16)
    assert result == '5'

def test_to_base_255_16():
    from solution import to_base
    result = to_base(255, 16)
    assert result == 'FF'

def test_to_base_1_any_base():
    from solution import to_base
    result = to_base(1, 10)
    assert result == '1'

def test_to_base_return_type():
    from solution import to_base
    result = to_base(31, 16)
    assert isinstance(result, str)

def test_to_base_9_2_palindrome():
    from solution import to_base
    result = to_base(9, 2)
    assert result == '1001'

def test_to_base_5_4():
    from solution import to_base
    result = to_base(5, 4)
    assert result == '11'

def test_to_base_boundary_b36():
    from solution import to_base
    result = to_base(35, 36)
    assert result == 'Z'

def test_to_base_all_digits_uppercase():
    from solution import to_base
    result = to_base(35, 36)
    assert result.isupper() or result.isdigit()
