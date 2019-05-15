a=int(input())
r=1
m=[]
for i in range(a):
    m.append("1"*r)
    r=r+2
for i in range(a):
    print(*m[i])
