def solve(sessions):
    events={}
    for start,end in sessions:
        if start>=end:
            continue
        events[start]=events.get(start,0)+1
        events[end]=events.get(end,0)-1
    times=sorted(events); active=best=0; intervals=[]
    for i,t in enumerate(times[:-1]):
        active += events[t]
        end=times[i+1]
        if active>best:
            best=active; intervals=[(t,end)]
        elif active==best and best>0:
            if intervals and intervals[-1][1]==t:
                intervals[-1]=(intervals[-1][0],end)
            else:
                intervals.append((t,end))
    return best, intervals
