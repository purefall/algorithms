def solve(sessions, horizon):
    delta=[0]*(horizon+1)
    for start,end in sessions:
        delta[start]+=1; delta[end]-=1
    active=best=0
    for change in delta:
        active+=change; best=max(best,active)
    return best
