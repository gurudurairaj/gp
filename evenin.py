a=int(input())
b=list(map(int,input().split()))
b.insert(0,0)
d=[]
for i in range(len(b)):
    if i%2==0:
        d.append(b[i])
for i in range(10):
    if len(d)==2:
        break
    g=len(d)
    for i in range(len(d)):
        if i%2==0:
            d.append(d[i])
    del d[0:g]
print(b.index(d[1])-1)
