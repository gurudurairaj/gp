h,n=map(int,input().split())
for i in range(1,1000):
    if n**i==h:
        print("yes")
        break
    if n**i>h:
        print("no")
        break
        
