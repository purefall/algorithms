def solve(nums, k):
    a = sorted(nums); left = 0; right = len(a)-1; total = 0
    while left < right:
        if a[left]+a[right] < k:
            total += right-left
            left += 1
        else:
            right -= 1
    return total
