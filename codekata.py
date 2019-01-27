k=input()
l=input()
a=[]
b=[]
z=97
a.append(0)
for i in range(26):
    a.append(chr(z))
    z=z+1
z=97
for i in range(26):
    a.append(chr(z))
    z=z+1
for i in range(len(k)):
    s=a.index(k[i])
    t=a.index(l[i])
    z=s+t
    b.append(a[z])
print("".join(b))
    
    
    


