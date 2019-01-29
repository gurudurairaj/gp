a=int(input())
j=[]
b=list(map(int,input().split()))
for i in range(a):
    if i==b[i]:
        j.append(b[i])
if len(j)!=0:
    j.sort()
    print(*j)
else:
    print("-1")
        
