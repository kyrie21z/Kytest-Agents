# Accepted by submit_tests; explanations in testgen_report.json.

def test_p3_minimal_num():
    ("Converts minimal valid integer 1 in base 10.\n\n    Docstring quote:\n        Precondition: num > 0, 2 <= b <= 36.\n\n    Input domain:\n        num=1 (lower boundary of num>0), b=10 (valid base).\n\n    Oracle:\n        1 in any base >= 2 is always '1'. Single-digit number.\n\n    Fault hypothesis:\n        Edge case: if loop condition or initial state mishandles num=1,\n        it might return empty string or wrong value.\n    ",)
    from solution import to_base
    result = to_base(1, 10)
    assert result == '1'
    assert isinstance(result, str)

def test_p4_minimal_base():
    ("Converts 5 using minimal valid base 2.\n\n    Docstring quote:\n        Precondition: num > 0, 2 <= b <= 36.\n\n    Input domain:\n        num=5 (>0), b=2 (lower boundary of base range).\n\n    Oracle:\n        5 = 1*4 + 0*2 + 1*1 => binary '101'.\n\n    Fault hypothesis:\n        Reversed digit order would produce '101' (palindrome, same either way),\n        but wrong digit mapping would still be caught by length/value check.\n    ",)
    from solution import to_base
    result = to_base(5, 2)
    assert result == '101'
    assert len(result) == 3

def test_p5_maximal_base():
    ("Converts 35 using maximal valid base 36.\n\n    Docstring quote:\n        Precondition:\n        num > 0, 2 <= b <= 36.\n\n    Input domain:\n        num=35 (>0), b=36 (upper boundary of base range).\n\n    Oracle:\n        35 < 36, so it is a single digit. In base-36, digit 35 maps to 'Z'\n        (alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ').\n\n    Fault hypothesis:\n        Wrong alphabet indexing or off-by-one would produce wrong character.\n    ",)
    from solution import to_base
    result = to_base(35, 36)
    assert result == 'Z'
    assert isinstance(result, str)

def test_extra_single_digit_all_bases():
    ("Single-digit inputs should return the corresponding digit character.\n\n    Docstring quote:\n        Precondition:\n        num > 0, 2 <= b <= 36.\n\n    Input domain:\n        num=7, tested across multiple bases where 7 < b, ensuring single digit.\n\n    Oracle:\n        When num < b, the result is a single character: alphabet[num].\n        For num=7, alphabet[7] = '7'.\n\n    Fault hypothesis:\n        Wrong alphabet indexing or off-by-one would produce wrong character.\n    ",)
    from solution import to_base
    for b in [8, 10, 16, 36]:
        result = to_base(7, b)
        assert result == '7', f'Failed for base {b}: got {result!r}'
        assert isinstance(result, str)

def test_extra_return_type():
    ('Verify return type is always a string.\n\n    Docstring quote:\n        Output:\n        A string representing the value of num in base b.\n\n    Input domain:\n        Various valid inputs covering boundary and normal cases.\n\n    Oracle:\n        Per contract, output must be a string for all valid inputs.\n\n    Fault hypothesis:\n        If implementation accidentally returns an int or other type,\n        this catches it.\n    ',)
    from solution import to_base
    for num, b in [(1, 2), (10, 2), (31, 16), (100, 8), (35, 36)]:
        result = to_base(num, b)
        assert isinstance(result, str), f'Expected str for to_base({num}, {b}), got {type(result)}'
