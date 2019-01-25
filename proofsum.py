n=int(input())
k=[]
f=0
g=0
q=0
w=n-1
su=0
suu=0
for i in range(n):
    print(i)
    a=list(map(int,input().split()))
    k.append(a)
for i in range(n):
    su=su+k[f][g]
    suu=suu+k[q][w]
    f=f+1
    g=g+1
    q=q+1
    w=w-1
print(su*suu)
