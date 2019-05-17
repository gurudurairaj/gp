n,m=map(int,input().split())
k=0
for i in range(n,m):
    a=str(i)
    s=0
    for h in range(len(a)):
        s=s+int(a[h])
        
    c=0
    for i in range(1,s):
        if s%i==0:
            c=c+1
    if c==1:
        k=k+1
        
print(k)
