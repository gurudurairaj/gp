n,m=(map(str,input().split()))
c=abs(len(n)-len(m))
for i in range(len(n)):
    if i>len(n) or i>len(m):
        break

    if n[i]!=m[i]:
        c=c+1
print(c)
