a,b,c=map(int,input().split())
d=[]
d.append(a)
d.append(b)
d.append(c)
d.sort()
if (d[0]*d[0])+(d[1]*d[1])==d[2]*d[2]:
    print("yes")
else:
    print("no")
