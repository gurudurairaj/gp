a=int(input())
c=0
for i in range(2,a):
    if a%i==0:
        c=c+1
        break
if c==1:
    print("yes")
else:
    print("no")


