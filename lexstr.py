a=input()
x=list(a)
x.sort(reverse=True)
s=a[0]
u=0
ii=""
for i in range(len(x)):
    if x[i]==s:
        break
    ss=x[i]
    f=a.index(ss)
    ss=a[f:len(a)]
    if len(ss)>u:
        u=len(ss)
        ii=ss
print(ii)
    
