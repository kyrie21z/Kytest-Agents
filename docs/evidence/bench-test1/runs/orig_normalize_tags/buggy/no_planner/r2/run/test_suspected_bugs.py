# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_order_preserved_non_alpha():
    """Verify that tags are returned in original (non-alphabetical) order.

    The docstring contract states: 'the remaining tags keep their original order.'
    Using 'Zebra, Apple' — after normalization ['zebra', 'apple'] — the output
    must preserve the input sequence, NOT sort alphabetically.

    Fault hypothesis: the implementation uses sorted(set(seen)), producing
    ['apple', 'zebra'] instead of the spec-required ['zebra', 'apple']."""
    from solution import normalize_tags
    result = normalize_tags('Zebra, Apple')
    # Original order: Zebra comes before Apple in input
    assert result == ['zebra', 'apple'], \
        f"Expected original-order ['zebra', 'apple'], got {result}"
    assert isinstance(result, list)
    assert len(result) == 2

def test_duplicates_first_wins_order():
    """Verify deduplication keeps first occurrence AND preserves original order.

    Input: 'Cherry, APPLE, cherry, Apple, Banana'
    Normalized first occurrences in order: cherry, apple, banana
    Expected: ['cherry', 'apple', 'banana'] (first-wins, original order)

    Fault hypothesis: sorted(set(seen)) produces ['apple', 'banana', 'cherry']
    (alphabetical), losing both the first-wins semantics and original order."""
    from solution import normalize_tags
    result = normalize_tags('Cherry, APPLE, cherry, Apple, Banana')
    # First occurrences in input order: Cherry->cherry, APPLE->apple, Banana->banana
    assert result == ['cherry', 'apple', 'banana'], \
        f"Expected first-wins order ['cherry', 'apple', 'banana'], got {result}"
    assert isinstance(result, list)
    assert len(result) == 3

def test_three_tags_reverse_alpha():
    """Test order preservation with three tags in reverse-alphabetical order.

    Input: 'Zebra, Mango, Apple'
    After normalization: ['zebra', 'mango', 'apple']
    Expected output: ['zebra', 'mango', 'apple'] (original order)

    Fault hypothesis: sorted(set(seen)) would produce ['apple', 'mango', 'zebra']
    (fully reversed), clearly violating the original-order guarantee."""
    from solution import normalize_tags
    result = normalize_tags('Zebra, Mango, Apple')
    assert result == ['zebra', 'mango', 'apple'], \
        f"Expected original-order ['zebra', 'mango', 'apple'], got {result}"
    assert isinstance(result, list)
    assert len(result) == 3
