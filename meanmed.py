a=int(input())
b=list(map(int,input().split()))
while len(b)!=0:
    if len(b)%2==0:
        a=len(b)//2
        c=(b[a]+b[a-1])//2
        print(c)
        a=a-1
        del b[a]
        del b[a]
    else:
        a=int(len(b)//2)
        print(b[a])
        del b[a]
