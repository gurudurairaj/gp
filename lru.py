a,b=map(int,input().split())
c=list(map(int,input().split()))
l=[]
for i in range(a):
    l.append(c[i])
    if len(l)>b:
        del l[0]
print(*l)

