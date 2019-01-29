n=int(input())
a=list(map(int,input().split()))
g={}
l=[]
for i in a:
    g[i]=0
for i in a:
    g[i]=g[i]+1
for i,j in g.items():
    if j==1:
        l.append(i)
print(*l)
        
