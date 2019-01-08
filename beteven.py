n,m=input().split()
n=int(n)
m=int(m)
ll=[]
for i in range(n+1,m):
    if i%2==0:
        ll.append(i)
print(*ll)
