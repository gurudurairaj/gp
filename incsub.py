n=int(input())
a=list(map(int,input().split()))
c=1
s=0
for i in range(n-1):
    if a[i]<a[i+1] and i==n-2:
        c=c+1
        if c>s:
            s=c
        
    elif a[i]<a[i+1]:
        c=c+1
    elif a[i]==a[i+1]:
        c=c
    elif a[i]>a[i+1]:
        if c>s:
            s=c
        c=1
print(s)
        
