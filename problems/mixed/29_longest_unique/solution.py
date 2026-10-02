def solve(events):
    last={}; left=best=0
    for right,event in enumerate(events):
        left=max(left,last.get(event,-1)+1)
        last[event]=right
        best=max(best,right-left+1)
    return best
