import operator
r=input()
f={}
for i in r:
    f[i]=0
for i in r:
    f[i]=f[i]+1
h=max(f.items(), key=operator.itemgetter(1))[0]
print(h)
