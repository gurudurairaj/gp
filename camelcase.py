m=list(map(str,input().split()))
c=0
for i in range(len(m)):
    a=m[i]
    if a[0].isupper():
        c=c+1
if c==len(m):
    print("yes")
else:
    print("no")
    
