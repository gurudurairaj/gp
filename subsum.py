a=input()
d=0
for i in range(1,len(a)+1):
    f=a[0:i]
    for i in range(len(f)):
        d=d+int(f[i])
        
print(d)
