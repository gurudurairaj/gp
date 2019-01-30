n=int(input())
pr=1
o=[]
a=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if i!=j:
            pr=pr*a[j]
    o.append(pr)
    pr=1
print(*o)
            
    
    
