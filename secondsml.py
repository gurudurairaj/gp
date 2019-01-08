n=int(input())
h=[]
for i in range(n):
    h.append(input())
for i in range(2):
    a=min(h)
    b=h.index(a)
    del h[b]
print(a)
