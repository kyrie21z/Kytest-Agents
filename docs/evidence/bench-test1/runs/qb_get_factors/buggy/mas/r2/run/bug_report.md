# Suspected implementation bugs

## test_p1_repeated_factors

- Plan P1: Factor a composite number with repeated prime factors — input `get_factors(100)`, expected `[2, 2, 5, 5]`
- Reviewer: Test follows spec expecting [2, 2, 5, 5]. Implementation fails because its fallback returns [] instead of [n] when the trial division loop finds no divisor, causing it to drop the final prime factor.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_p1_repeated_factors ___________________________
test_solution.py:13: in test_p1_repeated_factors
    assert result == [2, 2, 5, 5]
E   assert [2, 2, 5] == [2, 2, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_repeated_factors - assert [2, 2, 5] == [2, 2...
1 failed in 0.02s
```

## test_p4_smallest_prime

- Plan P4: Factor the smallest prime number at the precondition boundary — input `get_factors(2)`, expected `[2]`
- Reviewer: Test follows spec expecting [2]. Implementation returns [] because range(2, 2) is empty and falls through to the buggy return [].

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_p4_smallest_prime ____________________________
test_solution.py:13: in test_p4_smallest_prime
    assert result == [2]
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_smallest_prime - assert [] == [2]
1 failed in 0.03s
```

## test_p5_perfect_power

- Plan P5: Factor a perfect power of a prime — input `get_factors(8)`, expected `[2, 2, 2]`
- Reviewer: Test follows spec expecting [2, 2, 2]. The recursive call on the final factor (2) hits the empty loop fallback and drops the last 2.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_p5_perfect_power _____________________________
test_solution.py:13: in test_p5_perfect_power
    assert result == [2, 2, 2]
E   assert [2, 2] == [2, 2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_perfect_power - assert [2, 2] == [2, 2, 2]
1 failed in 0.03s
```

## test_p6_distinct_primes

- Plan P6: Factor a number with distinct prime factors — input `get_factors(6)`, expected `[2, 3]`
- Reviewer: Test follows spec expecting [2, 3]. The recursive call on 3 hits the empty loop fallback and returns [], dropping the factor 3.

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_p6_distinct_primes ____________________________
test_solution.py:13: in test_p6_distinct_primes
    assert result == [2, 3]
E   assert [2] == [2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_distinct_primes - assert [2] == [2, 3]
1 failed in 0.02s
```

## test_p7_mixed_factors_sorted

- Plan P7: Verify sorted order and repetition for mixed factors — input `get_factors(12)`, expected `[2, 2, 3]`
- Reviewer: Test follows spec expecting [2, 2, 3]. Same fallback bug causes the final prime factor 3 to be omitted.

```
[100%]
=================================== FAILURES ===================================
_________________________ test_p7_mixed_factors_sorted _________________________
test_solution.py:13: in test_p7_mixed_factors_sorted
    assert result == [2, 2, 3]
E   assert [2, 2] == [2, 2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p7_mixed_factors_sorted - assert [2, 2] == [2, ...
1 failed in 0.02s
```

## test_p2_prime_number

- Plan P2: Factor a prime number — input `get_factors(101)`, expected `[101]`
- Reviewer: Test follows spec expecting [101]. Implementation returns [] for primes due to the incorrect fallback after the loop.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p2_prime_number _____________________________
test_solution.py:13: in test_p2_prime_number
    assert result == [101]
E   assert [] == [101]
E     
E     Right contains one more item: 101
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_prime_number - assert [] == [101]
1 failed in 0.02s
```

## test_p8_larger_prime

- Plan P8: Factor a larger prime number — input `get_factors(997)`, expected `[997]`
- Reviewer: Test follows spec expecting [997]. Implementation returns [] for primes due to the incorrect fallback after the loop.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p8_larger_prime _____________________________
test_solution.py:13: in test_p8_larger_prime
    assert result == [997]
E   assert [] == [997]
E     
E     Right contains one more item: 997
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p8_larger_prime - assert [] == [997]
1 failed in 0.03s
```

## test_p9_multiple_distinct_primes

- Plan P9: Verify output length and values for multiple distinct primes — input `get_factors(30)`, expected `[2, 3, 5]`
- Reviewer: Test follows spec expecting [2, 3, 5]. The recursive step on 5 hits the empty loop fallback and drops the factor 5.

```
[100%]
=================================== FAILURES ===================================
_______________________ test_p9_multiple_distinct_primes _______________________
test_solution.py:13: in test_p9_multiple_distinct_primes
    assert result == [2, 3, 5]
E   assert [2, 3] == [2, 3, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p9_multiple_distinct_primes - assert [2, 3] == ...
1 failed in 0.02s
```

## test_extra_product_of_two_equal_primes

- Reviewer: Test follows spec expecting [7, 7]. The recursive call on 7 hits the empty loop fallback and drops the second 7.

```
[100%]
=================================== FAILURES ===================================
____________________ test_extra_product_of_two_equal_primes ____________________
test_solution.py:12: in test_extra_product_of_two_equal_primes
    assert result == [7, 7]
E   assert [7] == [7, 7]
E     
E     Right contains one more item: 7
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_product_of_two_equal_primes - assert [7] ...
1 failed in 0.02s
```

## test_extra_large_composite

- Reviewer: Test follows spec expecting [2, 2, 2, 5, 5, 5]. The recursive step on the final 5 hits the empty loop fallback and drops one 5.

```
[100%]
=================================== FAILURES ===================================
__________________________ test_extra_large_composite __________________________
test_solution.py:12: in test_extra_large_composite
    assert result == [2, 2, 2, 5, 5, 5]
E   assert [2, 2, 2, 5, 5] == [2, 2, 2, 5, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_large_composite - assert [2, 2, 2, 5, 5] ...
1 failed in 0.02s
```
