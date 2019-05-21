n,m=map(int,input().split())
z=list(map(int,input().split()))
a=[]
s=0
for i in range(m):
    x,y=map(int,input().split())
    s=0
    for j in range(x-1,y):
        s=s^z[j]
    a.append(s)
        
for i in range(len(a)):
    print(a[i])
