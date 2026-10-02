"""
Clarifications:
Baseline:
Approach and invariant:
Time:
Space:
Manual dry-run:
"""


def solve(nums: list[int], k: int) -> bool:

    last_seen = {}

    for ii, elem in enumerate(nums):
        last_seen_idx = last_seen.get(elem, -1)
        last_seen[elem] = ii

        if last_seen_idx >= 0 and abs(ii - last_seen_idx) <= k:
            return True

    return False


assert solve([4, 1, 7, 4], 3) == True
assert solve([4, 1, 7, 4], 2) == False
assert solve([5, 5], 1) == True
assert solve([], 1) == False
