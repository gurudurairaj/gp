n=int(input())
l=list(map(int,input().split()))
i=0
c=0
m=[]
while i <n:
    if l[i]==0:
        del l[i]
        n=n-1
        c=c+1
        i=i-1
    i=i+1
i=0
for i in range(c):
    m.append(0)
print(*(l+m))
