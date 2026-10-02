# 18. Top K Scores

records contains unique (customer_id, numeric_score), with no NaN scores. Return up to k records ordered by descending score, breaking ties by ascending ID. k <= 0 returns [].

## Function

```python
def solve(records, k):
    ...
```

## Example

Arguments: `([('a', 0.7), ('b', 0.9), ('c', 0.9)], 2)`

Output: `[('b', 0.9), ('c', 0.9)]`

## Your task

Clarify assumptions, describe a baseline, propose an improvement, code, manually dry-run, and state time and space costs. Assume inputs satisfy the stated contract.
