"""
Clarifications:
Baseline:
    - The simplest approach is for each element to find the substract from target within the rest of the list
    - This would give 0(n^2)
Approach and invariant:
Time:
Space:
Manual dry-run:
"""


def solve(nums: list, target: int) -> tuple[int, int] | None:
    """The idea is to find an element that satisfies target - nums[i],
    in the list nums[i+1:]

    Args:
        nums (_type_): _description_
        target (_type_): _description_

    Returns:
        tuple[int, int] | None: _description_
    """
    if nums is None or target is None:
        return None

    for ii, elem in enumerate(nums):
        substract = target - elem

        if substract in nums[ii + 1 :]:
            jj = nums[ii + 1 :].index(substract)
            return (ii, jj + ii + 1)

    return None


print(solve([1, 2, 3], 3))
breakpoint()
print(solve([1, 2, 3], 3))
