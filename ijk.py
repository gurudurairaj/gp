a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(len(b)):
    for j in range(i,len(b)):
        for k in range(j,len(b)):
            if b[i]>b[j]>b[k] and i<j<k:
                c=c+1
print(c)
