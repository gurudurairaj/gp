import math
n=int(input())
s=n
i=2
while i>1:
    a=math.log10(n)/math.log10(2)
    if 2**a==n:
        print(int(s-(2**a)))
        break
    else:
        n=n-1
