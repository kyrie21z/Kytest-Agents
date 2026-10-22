# Accepted by submit_tests; explanations in testgen_report.json.

from solution import get_factors as _case0_get_factors

def test_p1_empty_list():
    """P1: Returns an empty list for unit input.

    Docstring quote: '>>> get_factors(1)
[]'

    Input domain: n = 1 (smallest valid input per precondition n >= 1).

    Oracle reasoning: The docstring example explicitly states that get_factors(1)
    returns []. Since 1 has no prime factors, the result must be an empty list.

    Fault hypothesis: A faulty implementation might return [1] instead of [],
    treating 1 as a prime factor.
    """
    result = _case0_get_factors(1)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [], f'Expected [] for n=1, got {result}'

from solution import get_factors as _case1_get_factors

def test_p2_smallest_prime():
    """P2: Returns single-element list for smallest prime.

    Docstring quote: 'A list of the prime factors of n in sorted order with repetition'

    Input domain: n = 2 (the smallest prime number).

    Oracle reasoning: 2 is prime, so its only prime factor is itself. The output
    must be [2].

    Fault hypothesis: A faulty implementation might return [] for n=2, failing
    to recognize 2 as prime.
    """
    result = _case1_get_factors(2)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [2], f'Expected [2] for n=2, got {result}'

from solution import get_factors as _case2_get_factors

def test_p3_composite_with_repetition():
    """P3: Returns sorted list with repeated factors for composite.

    Docstring quote: '>>> get_factors(100)
[2, 2, 5, 5]'

    Input domain: n = 100 = 2^2 * 5^2.

    Oracle reasoning: 100 = 2 x 2 x 5 x 5. The function must return all prime
    factors with repetition in sorted order: [2, 2, 5, 5].

    Fault hypothesis: A faulty implementation might return distinct primes only
    [2, 5], missing the repetition requirement.
    """
    result = _case2_get_factors(100)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [2, 2, 5, 5], f'Expected [2, 2, 5, 5] for n=100, got {result}'

from solution import get_factors as _case3_get_factors

def test_p4_prime_input():
    """P4: Returns single-element list for prime input.

    Docstring quote: '>>> get_factors(101)
[101]'

    Input domain: n = 101 (a prime number).

    Oracle reasoning: 101 is prime, so its only prime factor is itself. The
    output must be [101].

    Fault hypothesis: A faulty implementation might incorrectly factor a prime
    into non-prime components or return [].
    """
    result = _case3_get_factors(101)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [101], f'Expected [101] for n=101, got {result}'

from solution import get_factors as _case4_get_factors

def test_p5_prime_power():
    """P5: Returns list with triple repetition for prime power.

    Docstring quote: 'A list of the prime factors of n in sorted order with repetition'

    Input domain: n = 8 = 2^3.

    Oracle reasoning: 8 = 2 x 2 x 2. With repetition, the output must be
    [2, 2, 2].

    Fault hypothesis: A faulty implementation might return [2] (distinct only)
    or [2, 4] (not all prime).
    """
    result = _case4_get_factors(8)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [2, 2, 2], f'Expected [2, 2, 2] for n=8, got {result}'

from solution import get_factors as _case5_get_factors

def test_p6_semiprime_sorted():
    """P6: Returns sorted distinct primes for semiprime.

    Docstring quote: 'A list of the prime factors of n in sorted order with repetition'

    Input domain: n = 6 = 2 x 3.

    Oracle reasoning: 6 = 2 x 3, two distinct primes. In sorted order with
    repetition: [2, 3].

    Fault hypothesis: A faulty implementation might return [3, 2] (wrong order)
    or [6] (not factored).
    """
    result = _case5_get_factors(6)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [2, 3], f'Expected [2, 3] for n=6, got {result}'

from solution import get_factors as _case6_get_factors

def test_p8_perfect_square_of_larger_prime():
    """P8: Handles perfect square of larger prime.

    Docstring quote: 'A list of the prime factors of n in sorted order with repetition'

    Input domain: n = 49 = 7^2.

    Oracle reasoning: 49 = 7 x 7. The output must be [7, 7] - two repetitions
    of the prime 7, in sorted order.

    Fault hypothesis: A faulty implementation might return [7] (missing repetition)
    or [1, 49] / [49] (incorrect factorization).
    """
    result = _case6_get_factors(49)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [7, 7], f'Expected [7, 7] for n=49, got {result}'

from solution import get_factors as _case7_get_factors

def test_p7_factor_product_equals_n():
    """P7: Validates factor product equals original input.

    Docstring quote: 'A list of the prime factors of n in sorted order with repetition'

    Input domain: n = 30 = 2 x 3 x 5.

    Oracle reasoning: For any valid input n >= 1, the product of all returned
    factors must equal n. Expected result: [2, 3, 5], and 2 x 3 x 5 = 30.

    Fault hypothesis: A faulty implementation might return incomplete factors
    whose product does not equal n, or include non-prime numbers.
    """
    n = 30
    result = _case7_get_factors(n)
    assert isinstance(result, list), 'Return value must be a list'
    assert result == [2, 3, 5], f'Expected [2, 3, 5] for n=30, got {result}'
