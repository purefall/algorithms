def solve(nums, k):
    left=0; right=len(nums)-1; total=0
    while left<right:
        if nums[left]+nums[right]<k:
            total += right-left; left += 1
        else:
            right -= 1
    return total
