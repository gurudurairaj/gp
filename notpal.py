a=input()
c=len(a)
for i in range(len(a)):
    s=a[0:c]
    if s==s[::-1]:
        pass
    else:
        print(s)
        break
    c=c-1
