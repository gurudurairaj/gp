a=input()
q=0
i=0
sum=0
for i in range(1,len(a)+1):
    s=int(a[q:i])
    sum=sum+(s*s)
    q=q+1
print(sum) 
