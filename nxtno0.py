a=int(input())
v=a
g=str(a)
g=list(g)
g.sort()
c=0
for i in range(10000):
    v=v+1
    y=str(v)
    y=list(y)
    y.sort()
    if y==g:
        c=c+1
        print(v)
        break
if c==0:
    print("impossible")
