def solve(tree, target):
    if tree is None: return False
    value,left,right=tree
    if left is None and right is None: return value==target
    return solve(left,target-value) or solve(right,target-value)
