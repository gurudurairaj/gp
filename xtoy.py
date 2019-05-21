n,m=(map(str,input().split()))
c=abs(len(n)-len(m))
for i in range(len(n)):
    if len(m)==1 and m[i] in n:
        break
    if i>=len(n) or i>=len(m):
        break

    if n[i]!=m[i] and m[i]:
        c=c+1
print(c)

