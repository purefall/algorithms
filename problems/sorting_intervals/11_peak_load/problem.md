# 11. Peak Load and Earliest Interval

Sessions are half-open [start,end) integer intervals with start <= end. Ignore zero-length sessions. Return (peak_count, earliest maximal contiguous peak interval), using None if no users are active.

## Function

```python
def solve(sessions):
    ...
```

## Example

Arguments: `([(2, 10), (5, 8), (6, 12), (11, 15)],)`

Output: `(3, (6, 8))`

## Your task

Clarify assumptions, describe a baseline, propose an improvement, code, manually dry-run, and state time and space costs. Assume inputs satisfy the stated contract.
