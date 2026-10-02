import heapq
def solve(lists):
    heap=[]; out=[]
    for i,values in enumerate(lists):
        if values:
            heap.append((values[0],i,0))
    heapq.heapify(heap)
    while heap:
        value,i,j=heapq.heappop(heap); out.append(value)
        if j+1<len(lists[i]):
            heapq.heappush(heap,(lists[i][j+1],i,j+1))
    return out
