# 27. Pipeline Execution Order

nodes is a list of unique string IDs; each (A,B) means A must precede B and both are in nodes. Return a valid order, or None if cyclic. Use a min-heap for deterministic lexicographically smallest available-node selection.

## Function

```python
def solve(nodes, edges):
    ...
```

## Example

Arguments: `(['a', 'b', 'c'], [('a', 'c'), ('b', 'c')])`

Output: `['a', 'b', 'c']`

## Your task

Clarify assumptions, describe a baseline, propose an improvement, code, manually dry-run, and state time and space costs. Assume inputs satisfy the stated contract.
