n=int(input())
a=1
m=3
for i in range(1,1000):
    if n==a:
        k=a+2
        break
    if n<a:
        for i in range(a,-1,-1):
            if i%3==0:
                f=i
                break
        d=m//2-2
        k=d+2
        e=abs(d-n)
        k=abs(k-e)
        break
    a=a+m
    m=m*2
    
print(k)
