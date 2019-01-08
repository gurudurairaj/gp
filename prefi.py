a=int(input())
agf=[]
ind=[]
g=[]
for dd in range(a):
    d=input()
    i=0
    kk=1 
    j=kk
    c=0
    while i<len(d):
        c=0
        while j<=len(d):
            a=d[c:j]
            g.append(a)
            j=j+1
            c=c+1
        kk=kk+1
        j=kk
        i=i+1
for i in range(len(g)):
    for j in range(i+1,len(g)):
        if g[i]==g[j] and g[i] not in agf:
            agf.append(g[i])
li=sorted(agf,key=len)
alen=len(li[-1])
for i in li:
    if len(i)==alen:
        ind.append(i)
del agf[0:len(agf)]
for i in ind:
    ff=inp[1].find(i)
    agf.append(ff)
sss=min(agf)
sss=agf.index(sss)
print(ind[sss])
