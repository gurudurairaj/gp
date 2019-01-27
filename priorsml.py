n=int(input())
l=[]
a=list(map(int,input().split()))
for i in range(1,n+1):
    l.append(min(a[0:i]))
print(*l)
