d=input()
i=0
kk=1
j=kk
c=0
g=[]
lis=[]
while i<len(d):
    c=0
    while j<=len(d):
        a=d[c:j]
        if a not in g:
            if a==a[::-1]:
                g.append(a)
        j=j+1
        c=c+1
    kk=kk+1
    j=kk
    i=i+1
at=g[len(g)-1]
att=d.find(at)
for i in range(len(d)):
    if i>=att and i<=att+len(at)-1:
        pass
    else:
        lis.append(d[i])
print(len(lis))
