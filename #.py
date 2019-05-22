a=input()
b=input()
c=[]
d=[]
s=""
for i in range(len(a)-1):
    if a[i].isdigit() and a[i+1].isdigit():
        s=s+a[i]
  
    elif a[i].isdigit() and a[i+1].isdigit()==False:
        s=s+a[i]
        c.append(s)
        s=""
    if i==len(a)-2 and a[i+1].isdigit():
        s=s+a[i+1]
        c.append(s)
        
s=""
for i in range(len(b)-1):
    if b[i].isdigit() and b[i+1].isdigit():
        s=s+b[i]
    elif  b[i].isdigit() and b[i+1].isdigit()==False:
        s=s+b[i]
        d.append(s)
        s=""
    if i==len(b)-2 and b[i+1].isdigit():
        s=s+b[i+1]
        d.append(s)
u=0
v=0
for i in range(len(c)):
    u=u+int(c[i])
for i in range(len(d)):
    v=v+int(d[i])
if u>v:
    s=""
    for i in range(len(a)):
        if a[i]=="#":
            break
        else:
            s=s+a[i]
    print(s)
else:
    s=""
    for i in range(len(b)):
        if b[i]=="#":
            break
        else:
            s=s+b[i]
    print(s)
        
    
