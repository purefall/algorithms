def solve(a, b):
    i=j=0; total=0
    while i<len(a) and j<len(b):
        if a[i][0]==b[j][0]:
            total += a[i][1]*b[j][1]; i+=1; j+=1
        elif a[i][0]<b[j][0]:
            i+=1
        else:
            j+=1
    return total
