from collections import deque
def solve(tree):
    if tree is None:
        return []
    queue=deque([tree]); out=[]
    while queue:
        level=[]
        for _ in range(len(queue)):
            value,left,right=queue.popleft(); level.append(value)
            if left is not None: queue.append(left)
            if right is not None: queue.append(right)
        out.append(level)
    return out
