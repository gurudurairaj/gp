a=int(input())
j=[]
b=list(map(int,input().split()))
for i in range(a):
    if i==b[i]:
        j.append(b[i])
j.sort()
print(*j)
        
