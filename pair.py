n,m=map(int,input().split())
z=list(map(int,input().split()))
c=0
for i in range(len(z)):
    for j in range(i,len(z)):
        if z[i]+z[j]==m:
            c=c+1
            break
if c>0:
    print("yes")
else:
    print("no")
