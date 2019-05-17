ds,dd=map(str,input().split())
if len(ds)<len(dd):
    d=ds
    rr=dd
else:
    d=dd
    rr=ds
i=0
kk=1
j=kk
c=0
g=[]
while i<len(d):
    c=0
    while j<=len(d):
        a=d[c:j]
        if a not in g:
            g.append(a)
        j=j+1
        c=c+1
    kk=kk+1
    j=kk
    i=i+1
for i in range(len(g)-1,-1,-1):
    if rr.find(g[i])==-1:
        pass
    else:
        print(g[i])
        break

