n,m=map(int,input().split())
h=list(map(int,input().split()))
i=0
while i<len(h):
    if h[i]==m:
        del h[i]
    else:
        i=i+1
if len(h)==0:
    print("empty")
else:
    print(*h)
        
