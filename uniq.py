a={}
n=int(input())
h=[]
for i in range(n):
    p=input()
    h.append(p)
for i in range(n):
    a[h[i]]=0
for i in h:
    a[i]=a[i]+1
k = min(a.keys(), key=(lambda k: a[k]))
print(k)
