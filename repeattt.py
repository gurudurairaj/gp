a={}
n=int(input())
f=[]
v=[]
for i in range(n):
    f.append(input())
for i in f:
    a[i]=0
for i in f:
    a[i]=a[i]+1
print(a)
for key,value in a.items():
    if value>1:
        v.append(key)
v.sort()
print(*v)
        
