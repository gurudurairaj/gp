n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=0
for i in range(n):
    s=a[0]
    del a[0]
    a.append(s)
    if a==b:
       break
    else:
        d=d+1
print(d+1)   
