# Benchmark summary (144 jobs)

Means over jobs with bootstrap 95% intervals (resampling jobs). Small samples: descriptive only.

## Clean target (reference implementation)

| config | jobs | tests | bug kill rate | false-positive rate (legal alts) | false bug reports |
|---|---|---|---|---|---|
| mas | 18 | 9.2 [7.2, 11.1] | 81% [65%, 96%] | 19% [3%, 39%] | 0.0 [0.0, 0.0] |
| no_planner | 18 | 7.6 [6.3, 9.0] | 76% [60%, 90%] | 14% [0%, 31%] | 0.2 [0.0, 0.7] |
| no_reviewer | 18 | 9.1 [7.4, 10.7] | 80% [64%, 93%] | 6% [0%, 17%] | 0.0 [0.0, 0.0] |
| single | 18 | 7.9 [6.3, 9.7] | 80% [67%, 92%] | 22% [6%, 44%] | 0.0 [0.0, 0.0] |

## Buggy target (primary bug planted; oracle-contamination probe)

| config | jobs | bug reported | fossilized (bug baked into accepted tests) | false reports |
|---|---|---|---|---|
| mas | 18 | 89% [72%, 100%] | 0% [0%, 0%] | 0.1 [0.0, 0.3] |
| no_planner | 18 | 83% [67%, 100%] | 67% [44%, 89%] | 0.0 [0.0, 0.0] |
| no_reviewer | 18 | 0% [0%, 0%] | 0% [0%, 0%] | 0.0 [0.0, 0.0] |
| single | 18 | 0% [0%, 0%] | 56% [33%, 78%] | 0.0 [0.0, 0.0] |

## Cost per job

| config | seconds | tokens | LLM calls (all roles) |
|---|---|---|---|
| mas | 252.0 [219.9, 285.6] | 90982.1 [79311.4, 103257.3] | 12.7 [11.2, 14.2] |
| no_planner | 203.9 [170.7, 239.7] | 76245.7 [62656.8, 90387.5] | 12.5 [10.7, 14.4] |
| no_reviewer | 215.7 [179.8, 252.9] | 70947.4 [63919.4, 78277.5] | 9.6 [8.8, 10.4] |
| single | 118.9 [94.1, 147.4] | 43952.7 [38697.1, 49376.4] | 6.6 [6.1, 7.1] |

## Per task

| task | tier | condition | config | status | tests | kill | fp | reported | fossilized |
|---|---|---|---|---|---|---|---|---|---|
| bcb_factorial_sums | T2 | buggy | mas | forced | 2 |  |  | False | False |
| bcb_factorial_sums | T2 | buggy | mas | forced | 2 |  |  | False | False |
| bcb_factorial_sums | T2 | buggy | no_planner | forced | 6 |  |  | False | True |
| bcb_factorial_sums | T2 | buggy | no_planner | forced | 4 |  |  | False | True |
| bcb_factorial_sums | T2 | buggy | no_reviewer | completed | 3 |  |  | False | False |
| bcb_factorial_sums | T2 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| bcb_factorial_sums | T2 | buggy | single | completed | 5 |  |  | False | True |
| bcb_factorial_sums | T2 | buggy | single | completed | 1 |  |  | False | False |
| bcb_factorial_sums | T2 | clean | mas | forced | 3 | 0.3333333333333333 | 0.0 |  |  |
| bcb_factorial_sums | T2 | clean | mas | forced | 2 | 0.3333333333333333 | 0.0 |  |  |
| bcb_factorial_sums | T2 | clean | no_planner | forced | 3 | 0.3333333333333333 | 0.0 |  |  |
| bcb_factorial_sums | T2 | clean | no_planner | forced | 4 | 0.6666666666666666 | 0.0 |  |  |
| bcb_factorial_sums | T2 | clean | no_reviewer | completed | 2 | 0.0 | 0.0 |  |  |
| bcb_factorial_sums | T2 | clean | no_reviewer | completed | 3 | 0.3333333333333333 | 0.0 |  |  |
| bcb_factorial_sums | T2 | clean | single | completed | 3 | 0.3333333333333333 | 0.0 |  |  |
| bcb_factorial_sums | T2 | clean | single | completed | 3 | 0.3333333333333333 | 0.0 |  |  |
| ce_bank_account | T3 | buggy | mas | accepted | 10 |  |  | True | False |
| ce_bank_account | T3 | buggy | mas | accepted | 11 |  |  | True | False |
| ce_bank_account | T3 | buggy | no_planner | accepted | 10 |  |  | True | True |
| ce_bank_account | T3 | buggy | no_planner | accepted | 6 |  |  | False | True |
| ce_bank_account | T3 | buggy | no_reviewer | completed | 11 |  |  | False | False |
| ce_bank_account | T3 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| ce_bank_account | T3 | buggy | single | completed | 6 |  |  | False | True |
| ce_bank_account | T3 | buggy | single | completed | 8 |  |  | False | True |
| ce_bank_account | T3 | clean | mas | accepted | 10 | 1.0 | 0.0 |  |  |
| ce_bank_account | T3 | clean | mas | accepted | 11 | 1.0 | 0.0 |  |  |
| ce_bank_account | T3 | clean | no_planner | forced | 8 | 0.0 | 0.0 |  |  |
| ce_bank_account | T3 | clean | no_planner | forced | 12 | 1.0 | 1.0 |  |  |
| ce_bank_account | T3 | clean | no_reviewer | completed | 10 | 1.0 | 0.0 |  |  |
| ce_bank_account | T3 | clean | no_reviewer | completed | 13 | 1.0 | 0.0 |  |  |
| ce_bank_account | T3 | clean | single | completed | 10 | 1.0 | 1.0 |  |  |
| ce_bank_account | T3 | clean | single | completed | 3 | 0.5 | 0.0 |  |  |
| ce_vending_machine | T5 | buggy | mas | accepted | 7 |  |  | True | False |
| ce_vending_machine | T5 | buggy | mas | accepted | 7 |  |  | True | False |
| ce_vending_machine | T5 | buggy | no_planner | accepted | 4 |  |  | True | False |
| ce_vending_machine | T5 | buggy | no_planner | accepted | 16 |  |  | True | True |
| ce_vending_machine | T5 | buggy | no_reviewer | completed | 10 |  |  | False | False |
| ce_vending_machine | T5 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| ce_vending_machine | T5 | buggy | single | completed | 6 |  |  | False | True |
| ce_vending_machine | T5 | buggy | single | completed | 9 |  |  | False | False |
| ce_vending_machine | T5 | clean | mas | accepted | 16 | 1.0 | 1.0 |  |  |
| ce_vending_machine | T5 | clean | mas | accepted | 10 | 1.0 | 1.0 |  |  |
| ce_vending_machine | T5 | clean | no_planner | accepted | 11 | 1.0 | 0.0 |  |  |
| ce_vending_machine | T5 | clean | no_planner | forced | 15 | 1.0 | 0.0 |  |  |
| ce_vending_machine | T5 | clean | no_reviewer | completed | 12 | 1.0 | 0.0 |  |  |
| ce_vending_machine | T5 | clean | no_reviewer | completed | 6 | 1.0 | 0.0 |  |  |
| ce_vending_machine | T5 | clean | single | completed | 11 | 1.0 | 0.0 |  |  |
| ce_vending_machine | T5 | clean | single | completed | 6 | 1.0 | 1.0 |  |  |
| ce_warehouse | T3 | buggy | mas | accepted | 9 |  |  | True | False |
| ce_warehouse | T3 | buggy | mas | accepted | 10 |  |  | True | False |
| ce_warehouse | T3 | buggy | no_planner | forced | 16 |  |  | True | True |
| ce_warehouse | T3 | buggy | no_planner | forced | 11 |  |  | True | True |
| ce_warehouse | T3 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| ce_warehouse | T3 | buggy | no_reviewer | completed | 11 |  |  | False | False |
| ce_warehouse | T3 | buggy | single | completed | 6 |  |  | False | True |
| ce_warehouse | T3 | buggy | single | completed | 10 |  |  | False | True |
| ce_warehouse | T3 | clean | mas | failed | 0 | 0.0 | 0.0 |  |  |
| ce_warehouse | T3 | clean | mas | accepted | 10 | 1.0 | 1.0 |  |  |
| ce_warehouse | T3 | clean | no_planner | accepted | 10 | 0.5 | 0.0 |  |  |
| ce_warehouse | T3 | clean | no_planner | forced | 9 | 0.5 | 1.0 |  |  |
| ce_warehouse | T3 | clean | no_reviewer | completed | 4 | 0.5 | 0.0 |  |  |
| ce_warehouse | T3 | clean | no_reviewer | completed | 12 | 0.5 | 1.0 |  |  |
| ce_warehouse | T3 | clean | single | completed | 6 | 0.5 | 1.0 |  |  |
| ce_warehouse | T3 | clean | single | completed | 13 | 1.0 | 1.0 |  |  |
| orig_allocate | T2 | buggy | mas | accepted | 12 |  |  | True | False |
| orig_allocate | T2 | buggy | mas | accepted | 10 |  |  | True | False |
| orig_allocate | T2 | buggy | no_planner | accepted | 9 |  |  | True | True |
| orig_allocate | T2 | buggy | no_planner | accepted | 7 |  |  | True | True |
| orig_allocate | T2 | buggy | no_reviewer | completed | 10 |  |  | False | False |
| orig_allocate | T2 | buggy | no_reviewer | completed | 13 |  |  | False | False |
| orig_allocate | T2 | buggy | single | completed | 6 |  |  | False | False |
| orig_allocate | T2 | buggy | single | completed | 6 |  |  | False | True |
| orig_allocate | T2 | clean | mas | accepted | 14 | 0.6666666666666666 | 0.0 |  |  |
| orig_allocate | T2 | clean | mas | accepted | 15 | 0.3333333333333333 | 0.0 |  |  |
| orig_allocate | T2 | clean | no_planner | accepted | 6 | 0.3333333333333333 | 0.0 |  |  |
| orig_allocate | T2 | clean | no_planner | accepted | 10 | 0.3333333333333333 | 0.0 |  |  |
| orig_allocate | T2 | clean | no_reviewer | completed | 12 | 0.3333333333333333 | 0.0 |  |  |
| orig_allocate | T2 | clean | no_reviewer | completed | 11 | 0.6666666666666666 | 0.0 |  |  |
| orig_allocate | T2 | clean | single | completed | 6 | 0.3333333333333333 | 0.0 |  |  |
| orig_allocate | T2 | clean | single | completed | 17 | 0.6666666666666666 | 0.0 |  |  |
| orig_normalize_tags | T5 | buggy | mas | accepted | 8 |  |  | True | False |
| orig_normalize_tags | T5 | buggy | mas | accepted | 8 |  |  | True | False |
| orig_normalize_tags | T5 | buggy | no_planner | accepted | 8 |  |  | True | True |
| orig_normalize_tags | T5 | buggy | no_planner | accepted | 11 |  |  | True | True |
| orig_normalize_tags | T5 | buggy | no_reviewer | completed | 10 |  |  | False | False |
| orig_normalize_tags | T5 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| orig_normalize_tags | T5 | buggy | single | completed | 6 |  |  | False | True |
| orig_normalize_tags | T5 | buggy | single | completed | 6 |  |  | False | True |
| orig_normalize_tags | T5 | clean | mas | accepted | 8 | 1.0 | 0.0 |  |  |
| orig_normalize_tags | T5 | clean | mas | accepted | 10 | 1.0 | 0.5 |  |  |
| orig_normalize_tags | T5 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| orig_normalize_tags | T5 | clean | no_planner | accepted | 6 | 1.0 | 0.5 |  |  |
| orig_normalize_tags | T5 | clean | no_reviewer | completed | 8 | 1.0 | 0.0 |  |  |
| orig_normalize_tags | T5 | clean | no_reviewer | completed | 12 | 1.0 | 0.0 |  |  |
| orig_normalize_tags | T5 | clean | single | completed | 6 | 1.0 | 0.0 |  |  |
| orig_normalize_tags | T5 | clean | single | completed | 6 | 0.6666666666666666 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | buggy | mas | accepted | 7 |  |  | True | False |
| qb_find_first_in_sorted | T2 | buggy | mas | accepted | 8 |  |  | True | False |
| qb_find_first_in_sorted | T2 | buggy | no_planner | accepted | 9 |  |  | True | False |
| qb_find_first_in_sorted | T2 | buggy | no_planner | accepted | 11 |  |  | True | False |
| qb_find_first_in_sorted | T2 | buggy | no_reviewer | completed | 7 |  |  | False | False |
| qb_find_first_in_sorted | T2 | buggy | no_reviewer | completed | 10 |  |  | False | False |
| qb_find_first_in_sorted | T2 | buggy | single | completed | 10 |  |  | False | False |
| qb_find_first_in_sorted | T2 | buggy | single | completed | 6 |  |  | False | False |
| qb_find_first_in_sorted | T2 | clean | mas | accepted | 8 | 1.0 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | clean | mas | accepted | 11 | 1.0 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | clean | no_reviewer | completed | 10 | 1.0 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | clean | no_reviewer | completed | 15 | 1.0 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | clean | single | completed | 6 | 1.0 | 0.0 |  |  |
| qb_find_first_in_sorted | T2 | clean | single | completed | 12 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | buggy | mas | forced | 1 |  |  | True | False |
| qb_get_factors | T2 | buggy | mas | accepted | 1 |  |  | True | False |
| qb_get_factors | T2 | buggy | no_planner | accepted | 8 |  |  | True | False |
| qb_get_factors | T2 | buggy | no_planner | accepted | 1 |  |  | True | False |
| qb_get_factors | T2 | buggy | no_reviewer | completed | 1 |  |  | False | False |
| qb_get_factors | T2 | buggy | no_reviewer | completed | 2 |  |  | False | False |
| qb_get_factors | T2 | buggy | single | completed | 3 |  |  | False | False |
| qb_get_factors | T2 | buggy | single | completed | 4 |  |  | False | False |
| qb_get_factors | T2 | clean | mas | accepted | 8 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | clean | mas | accepted | 10 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | clean | no_planner | accepted | 7 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | clean | no_reviewer | completed | 8 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | clean | no_reviewer | completed | 10 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | clean | single | completed | 10 | 1.0 | 0.0 |  |  |
| qb_get_factors | T2 | clean | single | completed | 10 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | buggy | mas | accepted | 2 |  |  | True | False |
| qb_shunting_yard | T2 | buggy | mas | accepted | 2 |  |  | True | False |
| qb_shunting_yard | T2 | buggy | no_planner | accepted | 2 |  |  | True | False |
| qb_shunting_yard | T2 | buggy | no_planner | forced | 6 |  |  | True | True |
| qb_shunting_yard | T2 | buggy | no_reviewer | completed | 2 |  |  | False | False |
| qb_shunting_yard | T2 | buggy | no_reviewer | completed | 2 |  |  | False | False |
| qb_shunting_yard | T2 | buggy | single | completed | 6 |  |  | False | True |
| qb_shunting_yard | T2 | buggy | single | completed | 13 |  |  | False | False |
| qb_shunting_yard | T2 | clean | mas | accepted | 12 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | clean | mas | accepted | 8 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | clean | no_reviewer | completed | 6 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | clean | no_reviewer | completed | 10 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | clean | single | completed | 8 | 1.0 | 0.0 |  |  |
| qb_shunting_yard | T2 | clean | single | completed | 6 | 1.0 | 0.0 |  |  |
