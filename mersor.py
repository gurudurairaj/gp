n=int(input())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        l.append(a[j])
l.sort()
print(*l)
    
