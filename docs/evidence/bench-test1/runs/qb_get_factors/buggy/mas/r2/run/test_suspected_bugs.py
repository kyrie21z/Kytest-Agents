# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import get_factors

def test_p1_repeated_factors():
    """Factor a composite number with repeated prime factors.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 100 (composite, precondition n >= 1 satisfied)
    Oracle: By definition, 100 = 2 * 2 * 5 * 5; the output must be [2, 2, 5, 5].
    Fault hypothesis: A buggy implementation might deduplicate factors or miss multiplicity,
        returning e.g. [2, 5] or [2, 5, 5].
    """
    result = get_factors(100)
    assert result == [2, 2, 5, 5]
    assert isinstance(result, list)

from solution import get_factors

def test_p4_smallest_prime():
    """Factor the smallest prime number at the precondition boundary.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 2 (smallest prime, precondition n >= 1 boundary)
    Oracle: 2 is prime; its only prime factor is 2; output must be [2].
    Fault hypothesis: The implementation may return [] for small primes due to
        the loop range(2, 2) being empty and falling through to return [].
    """
    result = get_factors(2)
    assert result == [2]
    assert isinstance(result, list)

from solution import get_factors

def test_p5_perfect_power():
    """Factor a perfect power of a prime.

    Contract quote: 'sorted order with repetition'
    Input domain: n = 8 = 2^3 (precondition n >= 1 satisfied)
    Oracle: 8 = 2 * 2 * 2; output must be [2, 2, 2].
    Fault hypothesis: Repeated factors might be collapsed to a single entry,
        returning [2] instead of [2, 2, 2].
    """
    result = get_factors(8)
    assert result == [2, 2, 2]
    assert isinstance(result, list)

from solution import get_factors

def test_p6_distinct_primes():
    """Factor a number with distinct prime factors.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 6 = 2 * 3 (precondition n >= 1 satisfied)
    Oracle: 6 = 2 * 3; output must be [2, 3] (sorted).
    Fault hypothesis: Factors might not be sorted, returning [3, 2], or one factor
        might be missing entirely.
    """
    result = get_factors(6)
    assert result == [2, 3]
    assert isinstance(result, list)

from solution import get_factors

def test_p7_mixed_factors_sorted():
    """Verify sorted order and repetition for mixed factors.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 12 = 2^2 * 3 (precondition n >= 1 satisfied)
    Oracle: 12 = 2 * 2 * 3; output must be [2, 2, 3] (sorted with multiplicity).
    Fault hypothesis: Multiplicity of 2 might be lost, yielding [2, 3]; or order
        might be wrong, yielding [2, 3, 2].
    """
    result = get_factors(12)
    assert result == [2, 2, 3]
    assert isinstance(result, list)

from solution import get_factors

def test_p2_prime_number():
    """Factor a prime number.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 101 (prime, precondition n >= 1 satisfied)
    Oracle: A prime number's only prime factor is itself; output must be [101].
    Fault hypothesis: The implementation may return [] for primes (fall-through bug),
        failing to include the prime itself as its own factor.
    """
    result = get_factors(101)
    assert result == [101]
    assert isinstance(result, list)

from solution import get_factors

def test_p8_larger_prime():
    """Factor a larger prime number.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 997 (large prime, precondition n >= 1 satisfied)
    Oracle: 997 is prime; output must be [997].
    Fault hypothesis: Large primes may incorrectly return [] due to the fall-through
        bug in the trial division loop.
    """
    result = get_factors(997)
    assert result == [997]
    assert isinstance(result, list)

from solution import get_factors

def test_p9_multiple_distinct_primes():
    """Verify output length and values for multiple distinct primes.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 30 = 2 * 3 * 5 (precondition n >= 1 satisfied)
    Oracle: 30 = 2 * 3 * 5; output must be [2, 3, 5] (three elements, sorted).
    Fault hypothesis: One of the three distinct factors might be omitted,
        yielding a list of length 2 instead of 3.
    """
    result = get_factors(30)
    assert result == [2, 3, 5]
    assert isinstance(result, list)

from solution import get_factors

def test_extra_product_of_two_equal_primes():
    """Factor the product of two equal primes (a square of a prime).

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 49 = 7^2 (precondition n >= 1 satisfied)
    Oracle: 49 = 7 * 7; output must be [7, 7].
    Fault hypothesis: Multiplicity may be lost, returning [7] instead of [7, 7].
    """
    result = get_factors(49)
    assert result == [7, 7]
    assert isinstance(result, list)

from solution import get_factors

def test_extra_large_composite():
    """Factor a large composite number.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 1000 = 2^3 * 5^3 (precondition n >= 1 satisfied)
    Oracle: 1000 = 2 * 2 * 2 * 5 * 5 * 5; output must be [2, 2, 2, 5, 5, 5].
    Fault hypothesis: Multiplicity of either prime may be partially or fully lost.
    """
    result = get_factors(1000)
    assert result == [2, 2, 2, 5, 5, 5]
    assert isinstance(result, list)
