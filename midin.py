n=int(input())
m=list(map(int,input().split()))
c=0
for i in range(1,n):
    if sum(m[0:i])==sum(m[i+1:len(m)]):
        c=c+1
        break
if c==1:
    print("yes")
else:
    print("no")
