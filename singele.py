a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    c.append(b.count(i))
for i in c:
    if i==1:
        y=c.index(i)
        print(b[y])
        break
    
