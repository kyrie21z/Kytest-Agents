# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_p1_standard_mixed():
    from solution import normalize_tags
    result = normalize_tags(" Python, ML ,python,, Data ")
    assert result == ['python', 'ml', 'data']

def test_p5_order_preservation():
    from solution import normalize_tags
    result = normalize_tags("B, A, b, a")
    assert result == ['b', 'a']
