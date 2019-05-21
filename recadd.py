n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            c=c+a[j]
print(c)
