#guru
n,m=map(int,input().split())
c=min(n,m)
d=max(n,m)
l=[]
h=[]
for i in range(c):
    a=list(map(int,input().split()))
    a.sort()
    l.append(a)
for i in range(d):
    for j in range(c):
        h.append(l[j][i])
    h.sort()
    for k in range(c):
        l[k][i]=h[k]
    del h[0:len(h)]
for i in range(c):
    print(*l[i])

        

