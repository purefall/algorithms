# Nearby Duplicate

Given a list of integers `nums` and a nonnegative integer `k`, return `True` if two distinct indices `i` and `j` satisfy both:

- `nums[i] == nums[j]`
- `abs(i - j) <= k`

Otherwise, return `False`. Negative numbers and duplicates are allowed. An empty list is valid. Assume inputs satisfy this contract.

## Function

```python
def solve(nums: list[int], k: int) -> bool:
    ...
```

## Examples

| nums | k | Output | Reason |
| --- | --- | --- | --- |
| `[4, 1, 7, 4]` | 3 | `True` | The two 4s are 3 positions apart. |
| `[4, 1, 7, 4]` | 2 | `False` | The two 4s are too far apart. |
| `[5, 5]` | 1 | `True` | Equal values at adjacent indices. |
| `[5, 5]` | 0 | `False` | Distinct indices cannot be 0 positions apart. |
| `[]` | 2 | `False` | There is no pair. |

## Your task

Describe a baseline, then try to improve it. Write down what information you need to remember as you scan the list, implement your approach, manually dry-run it, and state its time and space costs.

Include `[8, 2, 8, 8]` with `k = 1` in your manual dry-run.
