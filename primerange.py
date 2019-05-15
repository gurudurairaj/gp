n=int(input())
l=[]
for i in range(1,n):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        l.append(i)
if len(l)==0:
    print(0)
else:
    print(*l)
            
