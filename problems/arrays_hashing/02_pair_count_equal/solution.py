def solve(nums, target):
    counts = {}; total = 0
    for x in nums:
        total += counts.get(target-x, 0)
        counts[x] = counts.get(x, 0)+1
    return total
