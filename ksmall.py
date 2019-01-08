n,k=input().split()
h=[]
for i in range(int(n)):
    h.append(input())
for i in range(int(k)):
    a=min(h)
    b=h.index(a)
    del h[b]
print(a)
