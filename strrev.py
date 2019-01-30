n=int(input())
a=list(map(str,input().split()))
l=[]
for i in range(n-1,-1,-1):
    l.append(a[i])
    l.append("->")
del l[len(l)-1]
print("".join(l))
