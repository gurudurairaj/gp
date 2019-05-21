n,m=map(int,input().split())
z=list(map(int,input().split()))
a=[]
for i in range(m):
    x,y=map(int,input().split())
    a.append(sum(z[x-1:y]))
print(a)
