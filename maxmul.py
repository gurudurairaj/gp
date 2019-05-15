a=int(input())
b=list(map(int,input().split()))
d=b
i=0
kk=1
j=kk
c=0
ll=0
g=[]
su=1
mul=0
while i<len(d):
    c=0
    while j<=len(d):
        a=d[c:j]
        su=1
        for k in range(len(a)):
            su=su*a[k]
        if su>mul:
            mul=su
        
            
            
        j=j+1
        c=c+1
    kk=kk+1
    j=kk
    i=i+1
print(mul)

