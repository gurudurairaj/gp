n=int(input())
m=list(map(int,input().split()))
v=[]
for i in range(n):
    if i%2==0:
        if m[i]%2!=0:
            v.append(m[i])
    else:
        if m[i]%2==0:
            v.append(m[i])
print(*v)
