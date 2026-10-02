def solve(tree):
    if tree is None:
        return 0
    _,left,right=tree
    return 1+max(solve(left),solve(right))
