n=int(input())
s=list(map(int,input().split()))
f=[]
su=1
for i in range(n):
    for j in range(n):
        if j!=i:
            su=su*s[j]
    f.append(su)
    su=1
print(*f)
        
    
