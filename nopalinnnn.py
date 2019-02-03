a=int(input())
a=str(a)
a=list(a)
h=0
for i in range(len(a)):
    h=h+int(a[i])
h=str(h)
h=list(h)
    
if h==h[::-1]:
    print("YES")
else:
    print("NO")
