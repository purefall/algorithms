import math
def solve(a, b):
    na=math.sqrt(sum(x*x for x in a.values()))
    nb=math.sqrt(sum(x*x for x in b.values()))
    if na==0 or nb==0: return 0.0
    if len(a)>len(b): a,b=b,a
    dot=sum(value*b.get(index,0) for index,value in a.items())
    return dot/(na*nb)
