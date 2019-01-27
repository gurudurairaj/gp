a=input()
b={}
k=[]
a=list(a)
for i in a:
    b[i]=0
for i in a:
    b[i]=b[i]+1
for i,j in b.items():
    if j==1:
        k.append(i)
print("".join(k))
