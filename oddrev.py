f=list(map(str,input().split()))
for i in range(len(f)):
    if i%2!=0:
        a=f[i-1]
        f[i-1]=a[::-1]
print(*f)
