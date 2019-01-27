n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n//2):
    if len(a)!=0:
         s=max(a)
         l.append(s)
         f=a.index(s)
         del a[f]
         s=min(a)
         l.append(s)
         f=a.index(s)
         del a[f]
    if len(a)==1:
        l.append(a[0])
print(*l)
