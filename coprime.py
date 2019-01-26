c,d=input().split()
a,b=len(c),len(d)
import math
g=math.gcd(a,b)
if g==1:
    print("yes")
else:
    print("no")
