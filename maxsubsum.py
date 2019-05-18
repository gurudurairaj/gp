dd=int(input())
d=list(map(int,input().split()))
i=0
kk=1
j=kk
c=0
ll=0
g=[]
ans=-999
while i<len(d):
    c=0
    while j<=len(d):
        a=d[c:j]
        a=sum(a)
        if a>ans:
            ans=a
            
        j=j+1
        c=c+1
    kk=kk+1
    j=kk
    i=i+1
print(ans)

