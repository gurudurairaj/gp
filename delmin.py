n,m=map(str,input().split())
n=list(n)
y=0
b=""
c=999
for i in range(len(n)-int(m)):
    if m=="0":
        c=0
        break
    a=min(n[y:len(n)])
    b=b+a
    y=n.index(a)+1
if c==0:
    print("".join(n))
else:
    print(b)
    
