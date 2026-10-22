# Accepted by submit_tests; explanations in testgen_report.json.

def test_basic_hex_conversion():
    from solution import to_base
    assert to_base(31, 16) == '1F'

def test_binary_conversion():
    from solution import to_base
    assert to_base(10, 2) == '1010'

def test_single_digit_result():
    from solution import to_base
    assert to_base(5, 10) == '5'
    assert to_base(35, 36) == 'Z'

def test_power_of_base():
    from solution import to_base
    assert to_base(8, 2) == '1000'
    assert to_base(27, 3) == '1000'
    assert to_base(16, 16) == '10'

def test_boundary_min_num():
    from solution import to_base
    assert to_base(1, 2) == '1'
    assert to_base(1, 36) == '1'

def test_large_number_with_letters():
    from solution import to_base
    assert to_base(255, 16) == 'FF'
    assert to_base(1000, 16) == '3E8'
