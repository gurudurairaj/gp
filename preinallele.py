a,b=map(int,input().split())
c=[]
m=0
g=[]
for i in range(a):
    d=list(map(int,input().split()))
    c.append(d)
s=c[0]
for i in s:
    for j in range(0,len(c)):
        if i in c[j]:
            m=m+1
    if m==a:
        g.append(i)
    m=0
g.sort()
print(*g)


    
