u=97
l=[]
c=0
for i in range(26):
    l.append(chr(u))
    u=u+1
ip=input()
iip=ip.lower()
iip=list(iip)
for i in l:
    if i in iip:
        c=c+1
if c==26:
    print("yes")
else:
    print("no")
