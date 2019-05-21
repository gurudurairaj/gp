a=input()
x=list(a)
x.sort(reverse=True)
s=x[0]
f=a.index(s)
print(a[f:len(a)])
