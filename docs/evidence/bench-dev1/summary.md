# Benchmark summary (40 jobs)

Means over jobs with bootstrap 95% intervals (resampling jobs). Small samples: descriptive only.

## Clean target (reference implementation)

| config | jobs | tests | bug kill rate | false-positive rate (legal alts) | false bug reports |
|---|---|---|---|---|---|
| mas | 5 | 9.0 [6.4, 10.6] | 100% [100%, 100%] | 0% [0%, 0%] | 0.0 [0.0, 0.0] |
| no_planner | 5 | 7.0 [3.4, 10.8] | 90% [70%, 100%] | 0% [0%, 0%] | 0.0 [0.0, 0.0] |
| no_reviewer | 5 | 8.0 [4.2, 11.2] | 70% [30%, 100%] | 0% [0%, 0%] | 0.0 [0.0, 0.0] |
| single | 5 | 7.0 [6.0, 9.0] | 90% [70%, 100%] | 0% [0%, 0%] | 0.0 [0.0, 0.0] |

## Buggy target (primary bug planted; oracle-contamination probe)

| config | jobs | bug reported | fossilized (bug baked into accepted tests) | false reports |
|---|---|---|---|---|
| mas | 5 | 100% [100%, 100%] | 0% [0%, 0%] | 0.2 [0.0, 0.6] |
| no_planner | 5 | 60% [20%, 100%] | 40% [0%, 80%] | 0.2 [0.0, 0.6] |
| no_reviewer | 5 | 0% [0%, 0%] | 0% [0%, 0%] | 0.0 [0.0, 0.0] |
| single | 5 | 0% [0%, 0%] | 20% [0%, 60%] | 0.0 [0.0, 0.0] |

## Cost per job

| config | seconds | tokens | LLM calls (all roles) |
|---|---|---|---|
| mas | 201.3 [158.6, 242.7] | 74328.6 [58820.6, 90252.0] | 10.8 [8.6, 13.2] |
| no_planner | 190.0 [109.9, 317.3] | 49490.4 [42012.9, 57334.9] | 8.5 [7.6, 9.3] |
| no_reviewer | 150.9 [132.3, 170.2] | 51620.0 [45552.2, 58002.9] | 7.2 [6.6, 7.9] |
| single | 86.0 [57.7, 126.8] | 39327.2 [28696.7, 49843.2] | 6.2 [5.3, 7.2] |

## Per task

| task | tier | condition | config | status | tests | kill | fp | reported | fossilized |
|---|---|---|---|---|---|---|---|---|---|
| bcb_bigram_counts | T5 | buggy | mas | accepted | 7 |  |  | True | False |
| bcb_bigram_counts | T5 | buggy | no_planner | accepted | 5 |  |  | False | True |
| bcb_bigram_counts | T5 | buggy | no_reviewer | failed | 0 |  |  | False | False |
| bcb_bigram_counts | T5 | buggy | single | completed | 5 |  |  | False | True |
| bcb_bigram_counts | T5 | clean | mas | forced | 4 | 1.0 | 0.0 |  |  |
| bcb_bigram_counts | T5 | clean | no_planner | accepted | 1 | 1.0 | 0.0 |  |  |
| bcb_bigram_counts | T5 | clean | no_reviewer | completed | 1 | 0.0 | 0.0 |  |  |
| bcb_bigram_counts | T5 | clean | single | completed | 6 | 1.0 | 0.0 |  |  |
| ce_shopping_cart | T3 | buggy | mas | accepted | 6 |  |  | True | False |
| ce_shopping_cart | T3 | buggy | no_planner | forced | 9 |  |  | True | True |
| ce_shopping_cart | T3 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| ce_shopping_cart | T3 | buggy | single | completed | 2 |  |  | False | False |
| ce_shopping_cart | T3 | clean | mas | accepted | 10 | 1.0 | 0.0 |  |  |
| ce_shopping_cart | T3 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| ce_shopping_cart | T3 | clean | no_reviewer | completed | 10 | 1.0 | 0.0 |  |  |
| ce_shopping_cart | T3 | clean | single | completed | 11 | 1.0 | 0.0 |  |  |
| qb_kth | T2 | buggy | mas | forced | 12 |  |  | True | False |
| qb_kth | T2 | buggy | no_planner | forced | 3 |  |  | False | False |
| qb_kth | T2 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| qb_kth | T2 | buggy | single | completed | 13 |  |  | False | False |
| qb_kth | T2 | clean | mas | accepted | 10 | 1.0 | 0.0 |  |  |
| qb_kth | T2 | clean | no_planner | accepted | 8 | 1.0 | 0.0 |  |  |
| qb_kth | T2 | clean | no_reviewer | completed | 12 | 1.0 | 0.0 |  |  |
| qb_kth | T2 | clean | single | completed | 6 | 1.0 | 0.0 |  |  |
| qb_lis | T2 | buggy | mas | accepted | 9 |  |  | True | False |
| qb_lis | T2 | buggy | no_planner | accepted | 10 |  |  | True | False |
| qb_lis | T2 | buggy | no_reviewer | completed | 10 |  |  | False | False |
| qb_lis | T2 | buggy | single | completed | 5 |  |  | False | False |
| qb_lis | T2 | clean | mas | accepted | 11 | 1.0 | 0.0 |  |  |
| qb_lis | T2 | clean | no_planner | accepted | 14 | 0.5 | 0.0 |  |  |
| qb_lis | T2 | clean | no_reviewer | completed | 6 | 0.5 | 0.0 |  |  |
| qb_lis | T2 | clean | single | completed | 6 | 0.5 | 0.0 |  |  |
| qb_to_base | T2 | buggy | mas | accepted | 4 |  |  | True | False |
| qb_to_base | T2 | buggy | no_planner | accepted | 9 |  |  | True | False |
| qb_to_base | T2 | buggy | no_reviewer | completed | 5 |  |  | False | False |
| qb_to_base | T2 | buggy | single | completed | 8 |  |  | False | False |
| qb_to_base | T2 | clean | mas | accepted | 10 | 1.0 | 0.0 |  |  |
| qb_to_base | T2 | clean | no_planner | accepted | 6 | 1.0 | 0.0 |  |  |
| qb_to_base | T2 | clean | no_reviewer | completed | 11 | 1.0 | 0.0 |  |  |
| qb_to_base | T2 | clean | single | completed | 6 | 1.0 | 0.0 |  |  |
