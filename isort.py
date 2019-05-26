n=list(map(int,input().split()))
m=[]
for i in range(len(n)):
    m.append(n[i])
n.sort()
if n==m:
    print("yes")
else:
    print("no")

