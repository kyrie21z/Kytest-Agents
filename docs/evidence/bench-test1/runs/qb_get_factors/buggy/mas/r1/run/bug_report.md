# Suspected implementation bugs

## test_p4_distinct_primes

- Plan P4: Factor a composite with distinct prime factors — input `6`, expected `[2, 3]`
- Reviewer: Test follows specification. Implementation violates contract by returning [] for primes and incompletely factoring composites.

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_p4_distinct_primes ____________________________
test_solution.py:11: in test_p4_distinct_primes
    assert result == [2, 3]
E   assert [2] == [2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_distinct_primes - assert [2] == [2, 3]
1 failed in 0.03s
```

## test_p5_prime_power

- Plan P5: Factor a prime power — input `8`, expected `[2, 2, 2]`
- Reviewer: Test follows specification. Implementation violates contract by returning [] for primes and incompletely factoring composites.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p5_prime_power ______________________________
test_solution.py:11: in test_p5_prime_power
    assert result == [2, 2, 2]
E   assert [2, 2] == [2, 2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_prime_power - assert [2, 2] == [2, 2, 2]
1 failed in 0.02s
```

## test_p2_repeated_primes

- Plan P2: Factor a composite number with repeated prime factors — input `100`, expected `[2, 2, 5, 5]`
- Reviewer: Test follows specification. Implementation violates contract by returning [] for primes and incompletely factoring composites.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_p2_repeated_primes ____________________________
test_solution.py:13: in test_p2_repeated_primes
    assert result == [2, 2, 5, 5]
E   assert [2, 2, 5] == [2, 2, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_repeated_primes - assert [2, 2, 5] == [2, 2,...
1 failed in 0.03s
```

## test_p6_smallest_prime

- Plan P6: Factor the smallest prime — input `2`, expected `[2]`
- Reviewer: Test follows specification. Implementation violates contract by returning [] for primes and incompletely factoring composites.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_p6_smallest_prime ____________________________
test_solution.py:13: in test_p6_smallest_prime
    assert result == [2]
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_smallest_prime - assert [] == [2]
1 failed in 0.02s
```

## test_p7_mixed_composite

- Plan P7: Factor a mixed composite — input `12`, expected `[2, 2, 3]`
- Reviewer: Test follows specification. Implementation violates contract by returning [] for primes and incompletely factoring composites.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_p7_mixed_composite ____________________________
test_solution.py:11: in test_p7_mixed_composite
    assert result == [2, 2, 3]
E   assert [2, 2] == [2, 2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p7_mixed_composite - assert [2, 2] == [2, 2, 3]
1 failed in 0.02s
```

## test_p3_prime_number

- Plan P3: Factor a prime number — input `101`, expected `[101]`
- Reviewer: Test follows specification. Implementation violates contract by returning [] for primes and incompletely factoring composites.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p3_prime_number _____________________________
test_solution.py:12: in test_p3_prime_number
    assert result == [101]
E   assert [] == [101]
E     
E     Right contains one more item: 101
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p3_prime_number - assert [] == [101]
1 failed in 0.02s
```

## test_extra_large_prime

- Reviewer: Test follows specification. Implementation violates contract by returning [] for primes and incompletely factoring composites.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_extra_large_prime ____________________________
test_solution.py:11: in test_extra_large_prime
    assert result == [97]
E   assert [] == [97]
E     
E     Right contains one more item: 97
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_large_prime - assert [] == [97]
1 failed in 0.02s
```

## test_p2_composite_repeated

- Plan P2: Factor a composite number with repeated prime factors — input `100`, expected `[2, 2, 5, 5]`
- Reviewer: Test input and expected output strictly follow the specification. The implementation incorrectly returns [] when the remaining subproblem is prime, violating the contract to return all prime factors.

```
[100%]
=================================== FAILURES ===================================
__________________________ test_p2_composite_repeated __________________________
test_solution.py:12: in test_p2_composite_repeated
    assert result == [2, 2, 5, 5]
E   assert [2, 2, 5] == [2, 2, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_composite_repeated - assert [2, 2, 5] == [2,...
1 failed in 0.02s
```

## test_p4_distinct_primes

- Plan P4: Factor a composite with distinct prime factors — input `6`, expected `[2, 3]`
- Reviewer: Test input and expected output strictly follow the specification. The implementation fails to recurse correctly on the quotient, dropping the second prime factor.

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_p4_distinct_primes ____________________________
test_solution.py:11: in test_p4_distinct_primes
    assert result == [2, 3]
E   assert [2] == [2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_distinct_primes - assert [2] == [2, 3]
1 failed in 0.02s
```

## test_p3_prime

- Plan P3: Factor a prime number — input `101`, expected `[101]`
- Reviewer: Test input and expected output strictly follow the specification. The implementation returns [] for prime inputs instead of [n], directly contradicting the docstring example and contract.

```
F                                                                        [100%]
=================================== FAILURES ===================================
________________________________ test_p3_prime _________________________________
test_solution.py:12: in test_p3_prime
    assert result == [101]
E   assert [] == [101]
E     
E     Right contains one more item: 101
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p3_prime - assert [] == [101]
1 failed in 0.01s
```

## test_p5_prime_power

- Plan P5: Factor a prime power — input `8`, expected `[2, 2, 2]`
- Reviewer: Test input and expected output strictly follow the specification. The implementation truncates the factorization list upon reaching a prime during recursion.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p5_prime_power ______________________________
test_solution.py:12: in test_p5_prime_power
    assert result == [2, 2, 2]
E   assert [2, 2] == [2, 2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_prime_power - assert [2, 2] == [2, 2, 2]
1 failed in 0.01s
```

## test_p6_smallest_prime

- Plan P6: Factor the smallest prime — input `2`, expected `[2]`
- Reviewer: Test input and expected output strictly follow the specification. The implementation falls through to return [] for n=2 because the trial division loop range is empty, violating the contract.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_p6_smallest_prime ____________________________
test_solution.py:12: in test_p6_smallest_prime
    assert result == [2]
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_smallest_prime - assert [] == [2]
1 failed in 0.01s
```
