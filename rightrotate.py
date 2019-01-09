a,b=input().split()
a=int(a)
b=int(b)
l=[]
for i in range(a):
    l.append(input())
for i in range(b):
    s=l[-1]
    del l[-1]
    l.insert(0,s)
print(*l)
