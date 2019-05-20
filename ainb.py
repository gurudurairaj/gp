a,b=map(str,input().split())
d=a
i=0
kk=1
j=kk
c=0
g=[]
while i<len(d):
    c=0
    while j<=len(d):
        a=d[c:j]
        if a not in g and len(a)>1:
            g.append(a)
        j=j+1
        c=c+1
    kk=kk+1
    j=kk
    i=i+1
c=0
for i in range(len(g)):
    if g[i] in b:
        print("yes")
        c=c+1
        break
if c==0:
    print("no")
    
