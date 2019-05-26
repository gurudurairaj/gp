a,m=map(str,input().split())
a=list(a)
for i in range(int(m)):
    s=a[len(a)-1]
    del a[len(a)-1]
    a.insert(0,s)
print("".join(a))

