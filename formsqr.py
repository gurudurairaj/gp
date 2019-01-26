a=[]
for i in range(4):
    b=list(map(int,input().split()))
    a.append(b)
e=abs(a[1][1]-a[0][1])
f=abs(a[3][1]-a[2][1])
g=abs(a[3][0]-a[0][0])
h=abs(a[2][0]-a[1][0])
if e==f==g==h:
    print("yes")
else:
    print("no")
