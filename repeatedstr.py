import operator
r=input()
f={}
for i in r:
    f[i]=0
print(f)
for i in r:
    f[i]=f[i]+1
print(f)
h=max(f.items(), key=operator.itemgetter(1))[0]
print(h)
