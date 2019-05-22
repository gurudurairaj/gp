a=input()
c=list(map(int,input().split()))
v=0
for i in range(len(c)):
    for j in range(i,len(c)):
        if c[i]<c[j] and i<j:
            v=v+1
print(v)
