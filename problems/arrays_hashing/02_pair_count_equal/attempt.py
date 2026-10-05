"""
Clarifications:
Baseline:
Approach and invariant:
Time:
Space:
Manual dry-run:
"""


def solve(nums: list, target: int) -> tuple[int, int]:

    seen: dict[int, list] = {}
    count_occurences = 0
    for ii, elem in enumerate(nums):
        substract = target - elem
        indices: list = seen.get(substract, [])

        if len(indices) > 0:
            count_occurences += len(indices)
        seen[elem] = seen.get(elem, []) + [ii]

    return count_occurences


print(solve([1, 2, 3, 4, 3], 6))
assert solve([1, 2, 3, 4, 3], 6) == 2
assert solve([3, 3, 3], 6) == 3
