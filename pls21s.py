a,b=input().split()
c,d=input().split()
e,f=input().split()
if a==e==c:
    print("yes")
elif b==d==f:
    print("yes")
elif a==b and c==d and f==e:
    print("yes")
else:
    print("no")
    
