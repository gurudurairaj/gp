c=list(map(str,input().split()))
l=[]
for i in c:
    l.append(i[::-1])
print(*l)

