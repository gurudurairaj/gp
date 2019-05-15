n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if c>0:
        break
    for j in range(n):
        if a[i]+a[j]==m:
                  c=c+1
                  break
if c>0:
    print("YES")
else:
    print("NO")
