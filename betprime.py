n,m=input().split()
c=0
n=int(n)
m=int(m)
ll=[]
for i in range(n,m):
    f=i
    for j in range(1,f+1):
        if f%j==0:
            c=c+1
    if c==2:
        ll.append(f)
    c=0
print(*ll)

    
    
