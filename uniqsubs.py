d=input()
i=0
kk=1
j=kk
c=0
g=[]
ans=0
while i<len(d):
    c=0
    while j<=len(d):
        a=d[c:j]
        for u in range(len(a)):
            if a[u] not in g:
                g.append(a[u])
        if len(a)==len(g):
            if len(a)>ans:
                ans=len(a)
        del g[0:len(g)]
        
        
            
        j=j+1
        c=c+1
    kk=kk+1
    j=kk
    i=i+1
print(ans)

