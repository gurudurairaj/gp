n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
print(a)
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            b.append(i)
            b.append(j)
for i in range(0,len(b),2):
    for h in range(m):
        a[i][h]=0
    for h in range(n):
        a[h][i+1]=0
for i in range(n):
    print(*a[i])
