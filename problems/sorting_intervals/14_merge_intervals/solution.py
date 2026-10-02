def solve(intervals):
    out=[]
    for start,end in sorted(intervals):
        if out and start<=out[-1][1]:
            out[-1]=(out[-1][0],max(end,out[-1][1]))
        else:
            out.append((start,end))
    return out
