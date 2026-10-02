# 15. Asymmetric Sparse Dot Product

Sorted unique-index sparse vectors; large is much longer than small. Compute their dot product without scanning the whole large vector or copying its indices.

## Function

```python
def solve(large, small):
    ...
```

## Example

Arguments: `([(1, 3), (5, 2), (100, 4)], [(100, 5)])`

Output: `20`

## Your task

Clarify assumptions, describe a baseline, propose an improvement, code, manually dry-run, and state time and space costs. Assume inputs satisfy the stated contract.
