n,k=map(int,input().split())
g="-"
a=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]==k:
            g="8"
            break
    if g=="8":
        break
if g=="8":
    print("YES")
else:
    print("NO")
