a=input()
c=0
if a.count("@")==1 and a.count(".")==1 and a[len(a)-4:len(a)]==".com":
    s=""
    for i in range(len(a)):
        if a[i]=="@":
            break
        s=s+a[i]
    if len(s)>=3:
        c=c+1
    s=""
    v=a.index("@")
    for i in range(v+1,len(a)):
        if a[i]==".":
            break
        s=s+a[i]
    if len(s)>=4:
        c=c+1
    if c==2:
        print("YES")
    else:
        print("NO")
        
    
else:
    print("NO")
    
