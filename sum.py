n,k=input().split()
a=[]
s=0
for i in range(int(n)):
    p=int(input())
    a.append(p)
for i in range(int(k)):
    s=s+a[i]
print(s)
