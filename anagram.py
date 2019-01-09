a="kabali"
a=list(a)
a.sort()
n=int(input())
m=0
for i in range(n):
    k=input()
    k=list(k)
    k.sort()
    if k==a:
        m=m+1
print(m)
