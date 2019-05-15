a=input()
d=0
for i in range(0,len(a)):
    if i==len(a)-1:
        d=d+(int(a[i])**int(a[0]))
    else:
        d=d+(int(a[i])**int(a[i+1]))
print(d)
    
    
