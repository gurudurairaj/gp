b=int(input())
v=list(map(int,input().split()))
s=[]
for i in range(len(v)):
    c=max(v[i:len(v)])
    if c==v[i]:
        s.append(v[i])
#s.append(v[len(v)-1])
print(*s)
print(max(v))
