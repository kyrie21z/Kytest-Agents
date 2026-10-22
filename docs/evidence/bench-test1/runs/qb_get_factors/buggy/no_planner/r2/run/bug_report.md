# Suspected implementation bugs

## test_get_factors_100

- Reviewer: Implementation returns [2, 2, 5] instead of [2, 2, 5, 5]. The recursive call on a prime quotient returns [], causing missing factors. Violates spec.

```
[100%]
=================================== FAILURES ===================================
_____________________________ test_get_factors_100 _____________________________
test_solution.py:6: in test_get_factors_100
    assert result == [2, 2, 5, 5]
E   assert [2, 2, 5] == [2, 2, 5, 5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_100 - assert [2, 2, 5] == [2, 2, 5, 5]
1 failed in 0.03s
```

## test_get_factors_prime_101

- Reviewer: Implementation returns [] for prime 101. Spec requires [101].

```
F                                                                        [100%]
=================================== FAILURES ===================================
__________________________ test_get_factors_prime_101 __________________________
test_solution.py:6: in test_get_factors_prime_101
    assert result == [101]
E   assert [] == [101]
E     
E     Right contains one more item: 101
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_prime_101 - assert [] == [101]
1 failed in 0.02s
```

## test_get_factors_two

- Reviewer: Implementation returns [] for prime 2. Spec requires [2].

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_get_factors_two _____________________________
test_solution.py:6: in test_get_factors_two
    assert result == [2]
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_two - assert [] == [2]
1 failed in 0.02s
```

## test_get_factors_three

- Reviewer: Implementation returns [] for prime 3. Spec requires [3].

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_get_factors_three ____________________________
test_solution.py:6: in test_get_factors_three
    assert result == [3]
E   assert [] == [3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_three - assert [] == [3]
1 failed in 0.02s
```

## test_get_factors_six

- Reviewer: Implementation returns [2] instead of [2, 3]. Fails to include the second prime factor due to incorrect base case.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_get_factors_six _____________________________
test_solution.py:6: in test_get_factors_six
    assert result == [2, 3]
E   assert [2] == [2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_six - assert [2] == [2, 3]
1 failed in 0.02s
```

## test_get_factors_eight

- Reviewer: Implementation returns [2, 2] instead of [2, 2, 2]. Missing final factor due to recursive flaw.

```
[100%]
=================================== FAILURES ===================================
____________________________ test_get_factors_eight ____________________________
test_solution.py:6: in test_get_factors_eight
    assert result == [2, 2, 2]
E   assert [2, 2] == [2, 2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_eight - assert [2, 2] == [2, 2, 2]
1 failed in 0.03s
```

## test_get_factors_twelve

- Reviewer: Implementation returns [2, 2] instead of [2, 2, 3]. Missing factor due to recursive flaw.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_get_factors_twelve ____________________________
test_solution.py:6: in test_get_factors_twelve
    assert result == [2, 2, 3]
E   assert [2, 2] == [2, 2, 3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_twelve - assert [2, 2] == [2, 2, 3]
1 failed in 0.03s
```

## test_get_factors_four

- Reviewer: Implementation returns [2] instead of [2, 2]. Missing factor due to recursive flaw.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_get_factors_four _____________________________
test_solution.py:6: in test_get_factors_four
    assert result == [2, 2]
E   assert [2] == [2, 2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_four - assert [2] == [2, 2]
1 failed in 0.02s
```

## test_get_factors_prime_2

- Reviewer: Implementation returns [] for prime 2. Spec requires [2].

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_get_factors_prime_2 ___________________________
test_solution.py:6: in test_get_factors_prime_2
    assert result == [2]
E   assert [] == [2]
E     
E     Right contains one more item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_prime_2 - assert [] == [2]
1 failed in 0.02s
```

## test_get_factors_prime_3

- Reviewer: Implementation returns [] for prime 3. Spec requires [3].

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_get_factors_prime_3 ___________________________
test_solution.py:6: in test_get_factors_prime_3
    assert result == [3]
E   assert [] == [3]
E     
E     Right contains one more item: 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_prime_3 - assert [] == [3]
1 failed in 0.02s
```

## test_get_factors_prime_5

- Reviewer: Implementation returns [] for prime 5. Spec requires [5].

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_get_factors_prime_5 ___________________________
test_solution.py:6: in test_get_factors_prime_5
    assert result == [5]
E   assert [] == [5]
E     
E     Right contains one more item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_prime_5 - assert [] == [5]
1 failed in 0.02s
```

## test_get_factors_prime_7

- Reviewer: Implementation returns [] for prime 7. Spec requires [7].

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_get_factors_prime_7 ___________________________
test_solution.py:6: in test_get_factors_prime_7
    assert result == [7]
E   assert [] == [7]
E     
E     Right contains one more item: 7
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_get_factors_prime_7 - assert [] == [7]
1 failed in 0.02s
```
