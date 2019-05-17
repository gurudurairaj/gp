n=int(input())
l=[]
h=0
for i in range(2,n):
    c=0
    for j in range(1,i):
        if i%j==0:
            c=c+1
    if c==1:
        l.append(i)
for i in range(len(l)):
    if l[i]%10==3:
        h=h+l[i]
print(h)
    
    
