import math
a,b=map(int,input().split())
c=math.gcd(a,b)
if c==1:
    print("yes")
else:
    print("no")
