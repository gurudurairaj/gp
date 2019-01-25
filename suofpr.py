n=int(input())
k=[]
f=0
g=0
q=0
w=n-1
su=1
suu=1
for i in range(n):
    a=list(map(int,input().split()))
    k.append(a)
for i in range(n):
    su=su*k[f][g]
    suu=suu*k[q][w]
    f=f+1
    g=g+1
    q=q+1
    w=w-1
print(su+suu)
    
