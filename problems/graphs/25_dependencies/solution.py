def solve(edges, changed):
    graph={}
    for a,b in edges: graph.setdefault(a,[]).append(b)
    seen={changed}; stack=[changed]
    while stack:
        node=stack.pop()
        for nxt in graph.get(node,[]):
            if nxt not in seen:
                seen.add(nxt); stack.append(nxt)
    return sorted(seen-{changed})
