import math
n,m=(map(int,input().split()))
a=list(map(int,input().split()))
for i in range(m):
    c,d=(map(int,input().split()))
    h=0
    for j in range(c-1,d):
        h=math.gcd(h,a[j])
    print(h)
        
