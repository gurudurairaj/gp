n=int(input())
z=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in range(n):
    s=bin(z[i])
    s=s[2:len(s)]
    s=s.count("1")
    a.append(s)
#print(a)
for i in range(len(a)):
    s=max(a)
    ss=a.index(s)
    b.append(a[ss])
    a[ss]=-1
  
    c.append(z[ss])
#print(b)
for i in c:
    print(i)     


