a=input()
a=list(a)
b=[]
g=[]
g.append(0)
for i in range(len(a)):
    if a[i]==" ":
        b.append(i)
for i in range(len(a)):
    if a[i]!=" ":
        g.append(a[i])
for i in range(len(g)):
    if i%2!=0:
        g[i]=g[i].upper()
    
del g[0]
for i in range(len(b)):
    g.insert(b[i]," ")
print("".join(g))

