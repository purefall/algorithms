# 11b. Peak Memory and Earliest Interval

Each job is `(start, end, memory)`: it holds `memory` units of RAM during the half-open integer interval `[start, end)`. `start <= end`, and `memory` is a positive integer. Jobs may arrive in any order. Ignore zero-length jobs.

Return `(peak_memory, earliest maximal contiguous interval at peak_memory)`. Use `(0, None)` if no job is running at any time.

## Function

```python
def solve(jobs):
    ...
```

## Examples

| jobs | Output | Reason |
| --- | --- | --- |
| `[(1, 5, 2), (3, 8, 4), (4, 6, 3)]` | `(9, (4, 5))` | All three jobs overlap on `[4, 5)`: 2 + 4 + 3. |
| `[(0, 3, 1), (0, 3, 1), (0, 3, 1), (5, 6, 4)]` | `(4, (5, 6))` | Most jobs at once is not the most memory. |
| `[(1, 4, 5), (4, 6, 5)]` | `(5, (1, 6))` | Handoff at 4 keeps memory at 5, so the interval continues. |
| `[(1, 4, 5), (4, 6, 3)]` | `(5, (1, 4))` | Handoff at 4 drops memory, so the interval ends. |
| `[]` | `(0, None)` | Nothing runs. |

## Your task

Clarify assumptions, describe a baseline, propose an improvement, code, manually dry-run, and state time and space costs. Assume inputs satisfy the stated contract.

Include `[(1, 3, 2), (3, 5, 1), (3, 5, 1)]` in your manual dry-run.
