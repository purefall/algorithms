import heapq
def solve(nodes, edges):
    graph={x:set() for x in nodes}; degree={x:0 for x in nodes}
    for a,b in edges:
        if b not in graph[a]:
            graph[a].add(b); degree[b]+=1
    heap=[x for x in nodes if degree[x]==0]; heapq.heapify(heap); out=[]
    while heap:
        x=heapq.heappop(heap); out.append(x)
        for y in graph[x]:
            degree[y]-=1
            if degree[y]==0: heapq.heappush(heap,y)
    return out if len(out)==len(nodes) else None
