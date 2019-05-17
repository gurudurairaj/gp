n=int(input())
g=list(map(int,input().split()))
c=0
for i in range(len(g)):
    if g.count(g[i])>c:
        c=g.count(g[i])
        d=g[i]
print(d)
    
    
