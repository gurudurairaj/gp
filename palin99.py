a=input()
c=0
for i in range(len(a)):
    s=a[0:i]+a[i+1:len(a)]
    if s==s[::-1]:
        c=c+1
if c>1:
    print("YES")
else:
    print("NO")
