a,b=map(int,input().split())
c=0
for i in range(1,a+1):
    c=c+1
    if c>=b and i!=a:
        c=0
print(c)
