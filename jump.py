import math
n=int(input())
if n==1:
    print("YES")
elif n>1:
    s=math.log10(n)/math.log10(2)
    if math.ceil(s)==math.floor(s):
        print("YES")
    else:
        print("NO")
