d,j=input().split()
i=0
j=int(j)
c=0
g=[]
while j<=len(d):
    a=d[c:j]
    if a not in g:
        g.append(a)
    j=j+1
    c=c+1
print(*g)

