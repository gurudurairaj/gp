a=input()
c=list(map(int,input().split()))
v=0
for i in range(len(c)):
    for j in range(i,len(c)):
        for k in range(j,len(c)):
            if c[i]+c[j]==c[k] and i<j<k:
                v=v+1
print(v)
