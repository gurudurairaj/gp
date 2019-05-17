n,m,o=map(int,input().split())
c=0
for i in range(n,m):
    a=str(i)
    if a.find(str(o))==-1:
        pass
    else:
        c=c+1
print(c)
