a,b=input().split()
a=int(a)
b=int(b)
c=max(a,b)
m=a*b
for i in range(1,c+1):
    s=a*i
    if s%b==0:
        print(s)
        break
