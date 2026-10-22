# Test suite for solution.get_factors — implements plan items P2–P8.


def test_p2_composite_repeated():
    """P2: Factor a composite number with repeated prime factors.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 100, a valid integer >= 1.
    Oracle: 100 = 2^2 * 5^2, so the prime factors in sorted order with repetition are [2, 2, 5, 5].
    Fault hypothesis: If the implementation does not fully decompose after finding a factor
      (e.g., stops dividing out one copy of a factor), or if it returns [] for primes
      encountered during recursion, the result will be incorrect (e.g., [2, 2, 5]).
    """
    from solution import get_factors
    result = get_factors(100)
    assert result == [2, 2, 5, 5]
    assert isinstance(result, list)


def test_p3_prime():
    """P3: Factor a prime number.

    Contract quote: example '>>> get_factors(101) [101]'
    Input domain: n = 101, a valid prime integer >= 1.
    Oracle: A prime number's only prime factor is itself, so the result must be [101].
    Fault hypothesis: The implementation may fall through the trial-division loop and
      return [] instead of [n] for primes, since no divisor is found.
    """
    from solution import get_factors
    result = get_factors(101)
    assert result == [101]
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


def test_p5_prime_power():
    """P5: Factor a prime power.

    Contract quote: 'with repetition' in the output description.
    Input domain: n = 8, a valid integer >= 1.
    Oracle: 8 = 2^3, so the prime factors with repetition are [2, 2, 2].
    Fault hypothesis: The implementation may only extract one factor of 2 and then
      incorrectly recurse on 4, or return [] for the remaining sub-problem if it treats
      intermediate values as primes incorrectly.
    """
    from solution import get_factors
    result = get_factors(8)
    assert result == [2, 2, 2]
    assert isinstance(result, list)


def test_p6_smallest_prime():
    """P6: Factor the smallest prime.

    Contract quote: precondition 'n >= 1'; output is 'sorted list of prime factors'.
    Input domain: n = 2, the smallest prime and smallest valid input that is not 1.
    Oracle: 2 is prime, so its only prime factor is [2].
    Fault hypothesis: The loop range(2, int(2**0.5)+1) = range(2, 2) is empty, so the
      function falls through to return [] instead of [2].
    """
    from solution import get_factors
    result = get_factors(2)
    assert result == [2]
    assert isinstance(result, list)


def test_p7_mixed_composite():
    """P7: Factor a mixed composite with multiple prime bases.

    Contract quote: 'Sorted order with repetition for composites having multiple prime bases'.
    Input domain: n = 12, a valid integer >= 1.
    Oracle: 12 = 2^2 * 3, so the result is [2, 2, 3].
    Fault hypothesis: Similar to P5/P2, the implementation may not fully decompose
      repeated factors or may mishandle the recursive step.
    """
    from solution import get_factors
    result = get_factors(12)
    assert result == [2, 2, 3]
    assert isinstance(result, list)


def test_p8_multiplicative_property():
    """P8: Verify multiplicative inverse property of factorization.

    Contract quote: 'Prime factors of n in sorted order with repetition'.
    Input domain: n = 30, a valid integer >= 1.
    Oracle: 30 = 2 * 3 * 5, so the result is [2, 3, 5]. Additionally, the product of
      all elements in the returned list must equal the original input n (multiplicative
      inverse property of prime factorization).
    Fault hypothesis: If any factor is missing or extra, the product check will catch it.
      Also verifies correct handling of three distinct prime factors.
    """
    from solution import get_factors
    result = get_factors(30)
    assert result == [2, 3, 5]
    assert isinstance(result, list)
    # Multiplicative property: product of factors equals original number
    product = 1
    for f in result:
        product *= f
    assert product == 30
