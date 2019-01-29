n=int(input())
a=[]
for i in range(n):
    v=list(map(int,input().split()))
    a.append(v)
c=0
d=0
s=0
for i in range(n):
    s=s+a[c][d]
    c=c+1
    d=d+1
print(s)
    
