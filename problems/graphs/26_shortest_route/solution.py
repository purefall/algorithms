from collections import deque
def solve(edges, start, goal):
    graph={}
    for a,b in edges:
        graph.setdefault(a,[]).append(b); graph.setdefault(b,[]).append(a)
    queue=deque([(start,0)]); seen={start}
    while queue:
        node,d=queue.popleft()
        if node==goal: return d
        for nxt in graph.get(node,[]):
            if nxt not in seen:
                seen.add(nxt); queue.append((nxt,d+1))
    return None
