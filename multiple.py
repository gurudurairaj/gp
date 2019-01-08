n=int(input())
s=n
l=[]
for i in range(5):
    l.append(s)
    s=s+n
print(*l)
