def solve(nums, target):
    counts={0:1}; prefix=total=0
    for x in nums:
        prefix+=x
        total+=counts.get(prefix-target,0)
        counts[prefix]=counts.get(prefix,0)+1
    return total
