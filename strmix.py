n,m=map(str,input().split())
x=min(len(n),len(m))
if len(n)<len(m):
    g=m
else:
    g=n
f=""
for i in range(x):
    f=f+n[i]
    f=f+m[i]
h=1
for i in range(x,len(g)):
    f=f+str(h)+g[i]
    h=h+1
print(f)
    
