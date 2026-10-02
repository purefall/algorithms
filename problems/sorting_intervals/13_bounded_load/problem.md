# 13. Bounded Timestamp Peak

Integer half-open sessions satisfy 0 <= start <= end <= horizon. Return maximum simultaneous load, zero for no sessions.

## Function

```python
def solve(sessions, horizon):
    ...
```

## Example

Arguments: `([(0, 3), (1, 2)], 3)`

Output: `2`

## Your task

Clarify assumptions, describe a baseline, propose an improvement, code, manually dry-run, and state time and space costs. Assume inputs satisfy the stated contract.
