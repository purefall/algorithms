def solve(large, small):
    total=0
    for index,value in small:
        lo=0; hi=len(large)
        while lo<hi:
            mid=(lo+hi)//2
            if large[mid][0]<index:
                lo=mid+1
            else:
                hi=mid
        if lo<len(large) and large[lo][0]==index:
            total+=value*large[lo][1]
    return total
