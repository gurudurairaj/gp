v,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=0
for i in b:
    if i in a:
        d=d+1
if d==len(b):
    print("YES")
else:
    print("NO")
