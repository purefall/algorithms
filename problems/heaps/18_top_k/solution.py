import heapq
def solve(records, k):
    if k<=0:
        return []
    return heapq.nsmallest(k, records, key=lambda r: (-r[1], r[0]))
