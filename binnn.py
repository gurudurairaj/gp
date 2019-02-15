a=int(input())
g=""
l=[]
for i in range(2**a):
    x=bin(i).replace("0b","")
    if len(x)<a:
        z=str(x)
        d=a-len(x)
        for i in range(d):
            g=g+"0"
        g=g+x
        l.append(g)
        g=""
    else:
        l.append(x)
for i in l:
    print(i,end="\n")
        
            
