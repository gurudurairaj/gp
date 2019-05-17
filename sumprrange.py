g=int(input())
l=[]
f=0
for i in range(1,g):
    c=0
    for j in range(1,i):
        if i%j==0:
            c=c+1
    if c==1:
        l.append(i)
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==g and l[i]<=
        l[j]:
            f=f+1
print(f)
