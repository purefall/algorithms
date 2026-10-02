def solve(weights, days):
    if not weights:
        return 0
    lo=max(weights); hi=sum(weights)
    while lo<hi:
        mid=(lo+hi)//2; used=1; load=0
        for w in weights:
            if load+w>mid:
                used+=1; load=0
            load+=w
        if used<=days:
            hi=mid
        else:
            lo=mid+1
    return lo
