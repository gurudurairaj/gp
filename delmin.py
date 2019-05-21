n,m=map(str,input().split())
n=list(n)
s=min(n)
c=i=j=0
while i<100:
    #print("j")
    if c==int(m):
        print("".join(n))
        break
    if n[0]==s:
        j=len(n)-1
        while j>0:
            if c==int(m):
                break
            del n[len(n)-1]
            #print(n,"g")
            c=c+1
            #print("H",c)
            j=j-1
           
            
    else:
        del n[0]
        #print(n)
        c=c+1
        #print("H",c)
    i=i+1
