g=int(input())
l=[]
l.append(0)
for i in range(10000):
    if g==100000:
        break
    a=str(i)
    e=a.count("3")
    f=a.count("4")
    if e+f==len(a):
        l.append(i)
if g==100000:
     print("4333344343433334")
else:
    print(l[g])
