n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    a.append(input())
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
c.sort()
g=set(c)
print(*g)
