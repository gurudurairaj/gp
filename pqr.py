n,p,q,r=map(int,input().split())
b=list(map(int,input().split()))
s=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i<=j<=k:
                d=p*b[i]+q*b[j]+r*b[k]
            if d>s:
                s=d
print(s)
