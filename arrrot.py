a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(b):
    h=c[0]
    del c[0]
    c.append(h)
print(*c)
