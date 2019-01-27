b=int(input())
g=0

for i in range(1,b+1):
    ii=len(str(i))
    iy=0
    u=i
    while iy<ii:
        h=u%10
        u=u/10
        if int(h)==2:
            g=g+1
        iy=iy+1
print(g)
