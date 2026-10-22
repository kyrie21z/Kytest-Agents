# Suspected implementation bugs

## test_prime_two

- Reviewer: Test follows specification; implementation incorrectly returns [] for prime inputs.

```
F                                                                        [100%]
=================================== FAILURES ===================================
________________________________ test_prime_two ________________________________
test_solution.py:6: in test_prime_two
    assert result == [2]
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_prime_two - assert [] == [2]
1 failed in 0.02s
```

## test_square_of_two

- Reviewer: Test follows specification; implementation misses the second factor 2 due to incorrect base case handling.

```
F                                                                        [100%]
=================================== FAILURES ===================================
______________________________ test_square_of_two ______________________________
test_solution.py:6: in test_square_of_two
    assert result == [2, 2]
E   assert [2] == [2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_square_of_two - assert [2] == [2, 2]
1 failed in 0.02s
```

## test_cube_of_two

- Reviewer: Test follows specification; implementation misses the third factor 2 for the same reason.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_______________________________ test_cube_of_two _______________________________
test_solution.py:6: in test_cube_of_two
    assert result == [2, 2, 2]
E   assert [2, 2] == [2, 2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_cube_of_two - assert [2, 2] == [2, 2, 2]
1 failed in 0.02s
```

## test_prime_three

- Reviewer: Test follows specification; implementation incorrectly returns [] for prime inputs.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_______________________________ test_prime_three _______________________________
test_solution.py:6: in test_prime_three
    assert result == [3]
E   assert [] == [3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_prime_three - assert [] == [3]
1 failed in 0.02s
```

## test_docstring_100

- Reviewer: Test follows specification; implementation returns [2, 2, 5] instead of [2, 2, 5, 5] because it drops the final prime factor.

```
[100%]
=================================== FAILURES ===================================
______________________________ test_docstring_100 ______________________________
test_solution.py:6: in test_docstring_100
    assert result == [2, 2, 5, 5]
E   assert [2, 2, 5] == [2, 2, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_docstring_100 - assert [2, 2, 5] == [2, 2, 5, 5]
1 failed in 0.03s
```

## test_docstring_101

- Reviewer: Test follows specification; implementation incorrectly returns [] for prime inputs.

```
F                                                                        [100%]
=================================== FAILURES ===================================
______________________________ test_docstring_101 ______________________________
test_solution.py:6: in test_docstring_101
    assert result == [101]
E   assert [] == [101]
E     
E     Right contains one more item: 101
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_docstring_101 - assert [] == [101]
1 failed in 0.02s
```

## test_prime_seven

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
LURES ===================================
_______________________________ test_prime_seven _______________________________
test_solution.py:6: in test_prime_seven
    assert result == [7], f'get_factors(7) returned {result}, expected [7] for prime 7'
E   AssertionError: get_factors(7) returned [], expected [7] for prime 7
E   assert [] == [7]
E     
E     Right contains one more item: 7
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_prime_seven - AssertionError: get_factors(7) re...
1 failed in 0.01s
```

## test_composite_14

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
=== FAILURES ===================================
______________________________ test_composite_14 _______________________________
test_solution.py:6: in test_composite_14
    assert result == [2, 7], f'get_factors(14) returned {result}, expected [2, 7]'
E   AssertionError: get_factors(14) returned [2], expected [2, 7]
E   assert [2] == [2, 7]
E     
E     Right contains one more item: 7
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_composite_14 - AssertionError: get_factors(14) ...
1 failed in 0.01s
```

## test_composite_49

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
=== FAILURES ===================================
______________________________ test_composite_49 _______________________________
test_solution.py:6: in test_composite_49
    assert result == [7, 7], f'get_factors(49) returned {result}, expected [7, 7]'
E   AssertionError: get_factors(49) returned [7], expected [7, 7]
E   assert [7] == [7, 7]
E     
E     Right contains one more item: 7
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_composite_49 - AssertionError: get_factors(49) ...
1 failed in 0.01s
```

## test_composite_21

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
=== FAILURES ===================================
______________________________ test_composite_21 _______________________________
test_solution.py:6: in test_composite_21
    assert result == [3, 7], f'get_factors(21) returned {result}, expected [3, 7]'
E   AssertionError: get_factors(21) returned [3], expected [3, 7]
E   assert [3] == [3, 7]
E     
E     Right contains one more item: 7
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_composite_21 - AssertionError: get_factors(21) ...
1 failed in 0.01s
```

## test_prime_two

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
AILURES ===================================
________________________________ test_prime_two ________________________________
test_solution.py:6: in test_prime_two
    assert result == [2], f'get_factors(2) returned {result}, expected [2] for prime 2'
E   AssertionError: get_factors(2) returned [], expected [2] for prime 2
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_prime_two - AssertionError: get_factors(2) retu...
1 failed in 0.01s
```

## test_prime_101

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
=========
________________________________ test_prime_101 ________________________________
test_solution.py:6: in test_prime_101
    assert result == [101], f'get_factors(101) returned {result}, expected [101] as shown in docstring'
E   AssertionError: get_factors(101) returned [], expected [101] as shown in docstring
E   assert [] == [101]
E     
E     Right contains one more item: 101
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_prime_101 - AssertionError: get_factors(101) re...
1 failed in 0.01s
```

## test_prime_three

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
LURES ===================================
_______________________________ test_prime_three _______________________________
test_solution.py:6: in test_prime_three
    assert result == [3], f'get_factors(3) returned {result}, expected [3] for prime 3'
E   AssertionError: get_factors(3) returned [], expected [3] for prime 3
E   assert [] == [3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_prime_three - AssertionError: get_factors(3) re...
1 failed in 0.01s
```

## test_prime_eleven

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
===============================
______________________________ test_prime_eleven _______________________________
test_solution.py:6: in test_prime_eleven
    assert result == [11], f'get_factors(11) returned {result}, expected [11] for prime 11'
E   AssertionError: get_factors(11) returned [], expected [11] for prime 11
E   assert [] == [11]
E     
E     Right contains one more item: 11
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_prime_eleven - AssertionError: get_factors(11) ...
1 failed in 0.01s
```

## test_composite_6

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
====== FAILURES ===================================
_______________________________ test_composite_6 _______________________________
test_solution.py:6: in test_composite_6
    assert result == [2, 3], f'get_factors(6) returned {result}, expected [2, 3]'
E   AssertionError: get_factors(6) returned [2], expected [2, 3]
E   assert [2] == [2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_composite_6 - AssertionError: get_factors(6) re...
1 failed in 0.01s
```

## test_composite_15

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
=== FAILURES ===================================
______________________________ test_composite_15 _______________________________
test_solution.py:6: in test_composite_15
    assert result == [3, 5], f'get_factors(15) returned {result}, expected [3, 5]'
E   AssertionError: get_factors(15) returned [3], expected [3, 5]
E   assert [3] == [3, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_composite_15 - AssertionError: get_factors(15) ...
1 failed in 0.01s
```

## test_composite_100

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
=========
______________________________ test_composite_100 ______________________________
test_solution.py:6: in test_composite_100
    assert result == [2, 2, 5, 5], f'get_factors(100) returned {result}, expected [2, 2, 5, 5]'
E   AssertionError: get_factors(100) returned [2, 2, 5], expected [2, 2, 5, 5]
E   assert [2, 2, 5] == [2, 2, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_composite_100 - AssertionError: get_factors(100...
1 failed in 0.01s
```

## test_composite_8

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
=================================
_______________________________ test_composite_8 _______________________________
test_solution.py:6: in test_composite_8
    assert result == [2, 2, 2], f'get_factors(8) returned {result}, expected [2, 2, 2]'
E   AssertionError: get_factors(8) returned [2, 2], expected [2, 2, 2]
E   assert [2, 2] == [2, 2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_composite_8 - AssertionError: get_factors(8) re...
1 failed in 0.01s
```

## test_factor_100_matches_docstring

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
_________________ test_factor_100_matches_docstring _______________________
test_solution.py:6: in test_factor_100_matches_docstring
    assert result == [2, 2, 5, 5], f'get_factors(100) returned {result}, expected [2, 2, 5, 5]'
E   AssertionError: get_factors(100) returned [2, 2, 5], expected [2, 2, 5, 5]
E   assert [2, 2, 5] == [2, 2, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_factor_100_matches_docstring - AssertionError: ...
1 failed in 0.01s
```

## test_factor_101_matches_docstring

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
==================================
______________________ test_factor_101_matches_docstring _______________________
test_solution.py:6: in test_factor_101_matches_docstring
    assert result == [101], f'get_factors(101) returned {result}, expected [101]'
E   AssertionError: get_factors(101) returned [], expected [101]
E   assert [] == [101]
E     
E     Right contains one more item: 101
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_factor_101_matches_docstring - AssertionError: ...
1 failed in 0.01s
```

## test_factor_2_is_prime

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
============== FAILURES ===================================
____________________________ test_factor_2_is_prime ____________________________
test_solution.py:6: in test_factor_2_is_prime
    assert result == [2], f'get_factors(2) returned {result}, expected [2]'
E   AssertionError: get_factors(2) returned [], expected [2]
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_factor_2_is_prime - AssertionError: get_factors...
1 failed in 0.01s
```

## test_factor_6_has_two_factors

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
ES ===================================
________________________ test_factor_6_has_two_factors _________________________
test_solution.py:6: in test_factor_6_has_two_factors
    assert result == [2, 3], f'get_factors(6) returned {result}, expected [2, 3]'
E   AssertionError: get_factors(6) returned [2], expected [2, 3]
E   assert [2] == [2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_factor_6_has_two_factors - AssertionError: get_...
1 failed in 0.01s
```

## test_factor_8_has_three_factors

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
==================
_______________________ test_factor_8_has_three_factors ________________________
test_solution.py:6: in test_factor_8_has_three_factors
    assert result == [2, 2, 2], f'get_factors(8) returned {result}, expected [2, 2, 2]'
E   AssertionError: get_factors(8) returned [2, 2], expected [2, 2, 2]
E   assert [2, 2] == [2, 2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_factor_8_has_three_factors - AssertionError: ge...
1 failed in 0.01s
```

## test_factor_two_type_and_length

- Reviewer: Implementation violates specification by returning [] for prime numbers. It lacks a base case to return [n] when no divisor is found up to sqrt(n).

```
======================== FAILURES ===================================
_______________________ test_factor_two_type_and_length ________________________
test_solution.py:6: in test_factor_two_type_and_length
    assert len(result) == 1, f'get_factors(2) returned list of length {len(result)}, expected 1'
E   AssertionError: get_factors(2) returned list of length 0, expected 1
E   assert 0 == 1
E    +  where 0 = len([])
=========================== short test summary info ============================
FAILED test_solution.py::test_factor_two_type_and_length - AssertionError: ge...
1 failed in 0.01s
```

## test_factor_4_missing_factor

- Reviewer: Implementation violates specification by returning incomplete factor lists for composites. Missing base case causes recursive calls on primes to return [], truncating the factor list.

```
RES ===================================
_________________________ test_factor_4_missing_factor _________________________
test_solution.py:6: in test_factor_4_missing_factor
    assert result == [2, 2], f'get_factors(4) returned {result}, expected [2, 2]'
E   AssertionError: get_factors(4) returned [2], expected [2, 2]
E   assert [2] == [2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_factor_4_missing_factor - AssertionError: get_f...
1 failed in 0.01s
```
