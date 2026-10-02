# 25. Affected Components

Each (A,B) means B depends on A. Return sorted distinct downstream reachable components, excluding changed even if cycles exist.

## Function

```python
def solve(edges, changed):
    ...
```

## Example

Arguments: `([('a', 'b'), ('b', 'c'), ('c', 'a')], 'a')`

Output: `['b', 'c']`

## Your task

Clarify assumptions, describe a baseline, propose an improvement, code, manually dry-run, and state time and space costs. Assume inputs satisfy the stated contract.
