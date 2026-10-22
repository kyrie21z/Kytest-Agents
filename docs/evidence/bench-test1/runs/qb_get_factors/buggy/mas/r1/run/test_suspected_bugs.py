# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_p4_distinct_primes():
    """P4: Factor a composite with distinct prime factors, n=6 -> [2, 3].

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'.
    Input domain: n = 6 = 2 * 3, product of two distinct primes.
    Oracle: The prime factors are 2 and 3, each appearing once, sorted -> [2, 3].
    Fault hypothesis: Might return [3, 2] (unsorted) or [6] (not factored).
    """
    from solution import get_factors
    result = get_factors(6)
    assert result == [2, 3]
    assert isinstance(result, list)

def test_p5_prime_power():
    """P5: Factor a prime power, n=8 -> [2, 2, 2].

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'.
    Input domain: n = 8 = 2^3, a prime power.
    Oracle: Three copies of 2, sorted -> [2, 2, 2].
    Fault hypothesis: Might return [2] (unique factors only) or [2, 4] (not fully factored).
    """
    from solution import get_factors
    result = get_factors(8)
    assert result == [2, 2, 2]
    assert isinstance(result, list)

def test_p2_repeated_primes():
    """P2: Factor a composite number with repeated prime factors, n=100 -> [2, 2, 5, 5].

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    and example '>>> get_factors(100) [2, 2, 5, 5]'.
    Input domain: n = 100, a composite with two distinct prime bases each squared.
    Oracle: 100 = 2 * 2 * 5 * 5, so the returned list must be exactly [2, 2, 5, 5].
    Fault hypothesis: Implementation might miss repeated factors, return unique factors
      only, or fail to sort them.
    """
    from solution import get_factors
    result = get_factors(100)
    assert result == [2, 2, 5, 5]
    assert isinstance(result, list)

def test_p6_smallest_prime():
    """P6: Factor the smallest prime, n=2 -> [2].

    Contract quote: 'Precondition:' states 'n >= 1', and output is
    'A list of the prime factors of n in sorted order with repetition'.
    Input domain: n = 2, the smallest prime and smallest input that is not 1.
    Oracle: 2 is prime, so its only prime factor is [2].
    Fault hypothesis: Loop range(2, int(2**0.5)+1) = range(2, 2) is empty, so falls
      through to return [], missing the prime case entirely.
    """
    from solution import get_factors
    result = get_factors(2)
    assert result == [2]
    assert isinstance(result, list)

def test_p7_mixed_composite():
    """P7: Factor a mixed composite, n=12 -> [2, 2, 3].

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'.
    Input domain: n = 12 = 2^2 * 3, a composite with repeated and distinct factors.
    Oracle: Prime factors are 2, 2, 3 in sorted order -> [2, 2, 3].
    Fault hypothesis: Might return [2, 6], [3, 2, 2], or [2, 3] (missing one factor).
    """
    from solution import get_factors
    result = get_factors(12)
    assert result == [2, 2, 3]
    assert isinstance(result, list)

def test_p3_prime_number():
    """P3: Factor a prime number, n=101 -> [101].

    Contract quote: 'An int to factor' from the Input section of the docstring.
    Input domain: n = 101, a prime number greater than sqrt(n) threshold for small i.
    Oracle: A prime's only prime factor is itself, so the result must be [101].
    Fault hypothesis: The implementation may return [] for primes (bug on line 30 of
      solution.py where it returns [] instead of [n] when no divisor is found).
    """
    from solution import get_factors
    result = get_factors(101)
    assert result == [101]
    assert isinstance(result, list)

def test_extra_large_prime():
    """Extra: Factor a larger prime number, n=97 -> [97].

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'.
    Input domain: n = 97, a prime number where sqrt(97) ~ 9.8 so loop runs up to 9.
    Oracle: 97 is prime; its only prime factor is itself, so the result must be [97].
    Fault hypothesis: Same bug as P3/P6 — returns [] when no divisor is found.
    """
    from solution import get_factors
    result = get_factors(97)
    assert result == [97]
    assert isinstance(result, list)

def test_p2_composite_repeated():
    """P2: Factor a composite number with repeated prime factors.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 100, a valid integer >= 1.
    Oracle: 100 = 2^2 * 5^2, so the prime factors in sorted order with repetition are [2, 2, 5, 5].
    Fault hypothesis: If the implementation does not fully decompose after finding a factor,
      or if it returns [] for primes encountered during recursion, the result will be incorrect.
    """
    from solution import get_factors
    result = get_factors(100)
    assert result == [2, 2, 5, 5]
    assert isinstance(result, list)

def test_p4_distinct_primes():
    """P4: Factor a composite with distinct prime factors.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 6, a valid integer >= 1.
    Oracle: 6 = 2 * 3, both primes, so the result is [2, 3].
    Fault hypothesis: The implementation might miss one factor or fail to sort correctly.
    """
    from solution import get_factors
    result = get_factors(6)
    assert result == [2, 3]
    assert isinstance(result, list)

def test_p3_prime():
    """P3: Factor a prime number.

    Contract quote: '>>> get_factors(101)\n        [101]' from docstring examples.
    Input domain: n = 101, a valid prime integer >= 1.
    Oracle: A prime number's only prime factor is itself, so the result must be [101].
    Fault hypothesis: The implementation may fall through the trial-division loop and
      return [] instead of [n] for primes, since no divisor is found.
    """
    from solution import get_factors
    result = get_factors(101)
    assert result == [101]
    assert isinstance(result, list)

def test_p5_prime_power():
    """P5: Factor a prime power.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 8, a valid integer >= 1.
    Oracle: 8 = 2^3, so the prime factors with repetition are [2, 2, 2].
    Fault hypothesis: The implementation may only extract one factor of 2 and then
      incorrectly recurse on 4, or return [] for the remaining sub-problem.
    """
    from solution import get_factors
    result = get_factors(8)
    assert result == [2, 2, 2]
    assert isinstance(result, list)

def test_p6_smallest_prime():
    """P6: Factor the smallest prime.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 2, the smallest prime and smallest valid input that is not 1.
    Oracle: 2 is prime, so its only prime factor is [2].
    Fault hypothesis: The loop range(2, int(2**0.5)+1) = range(2, 2) is empty, so the
      function falls through to return [] instead of [2].
    """
    from solution import get_factors
    result = get_factors(2)
    assert result == [2]
    assert isinstance(result, list)
