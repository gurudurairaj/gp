n=int(input())
m=list(map(int,input().split()))
x={}
for i in m:
    x[i]=0
for i in m:
    x[i]=x[i]+1
h=min(x.items(), key=lambda x: x[1])
print(h[0])
