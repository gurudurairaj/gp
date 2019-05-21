n=int(input())
z=list(map(int,input().split()))
c=0
for i in range(1,len(z)):
    a=z[0:i]
    b=z[i:len(z)]
    if sum(a)//len(a)==sum(b)//len(b):
        c=c+1
        break
    
if c>0:
    print("yes")
else:
    print("no")
