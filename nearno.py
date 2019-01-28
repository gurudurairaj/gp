n,m=map(int,input().split())
a=list(map(int,input().split()))
b={}
c=0
l=[]
for i in a:
    b[i]=abs(m-i)
so=sorted(b.items(), key=lambda kv: kv[1])
for i in range(n):
    if so[i][1]!=0 and c<3:
        l.append(so[i][0])
        c=c+1
print(*l)
        
    
  
