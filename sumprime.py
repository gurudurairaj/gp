n=int(input())
l=[]
for i in range(1,n):
    c=0
    for j in range(1,i):
        if i%j==0:
            c=c+1
    if c==1:
        l.append(i)
for i in range(len(l)):
    for  j in range(i,len(l)):
        if l[i]+l[j]==n:
            print(l[i],l[j])
            break
    if l[i]+l[j]==n:
        break
