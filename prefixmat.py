n=int(input())
a=list(map(str,input().split()))
b=input()
c=0
for i in range(len(a)):
    d=a[i]
    if b==d[0:len(b)]:
        c=c+1
print(c)
    
