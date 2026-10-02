import heapq
def solve(values, k):
    heap=[]
    for value in values:
        if len(heap)<k:
            heapq.heappush(heap,value)
        elif value>heap[0]:
            heapq.heapreplace(heap,value)
    return heap[0] if len(heap)==k else None
