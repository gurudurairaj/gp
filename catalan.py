import math
n=int(input())
a=[]
for i in range(n+1):
    s=2*i
    s=math.factorial(s)
    f=math.factorial(i+1)
    g=math.factorial(i)
    h=s//(f*g)
    a.append(h)
print(*a)
    
