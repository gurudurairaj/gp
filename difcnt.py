a,v=map(int,input().split())
b=list(map(int,input().split()))
c=0
for i in range(len(b)):
    for j in range(i,len(b)):
        if abs(b[i]-b[j])==v:
            c=c+1
print(c)
    
