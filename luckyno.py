a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(1,len(b)+1):
    if i*a in b:
        c=c+1

print(c)
