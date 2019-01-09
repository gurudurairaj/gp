r=int(input())
d=input()
v=["a","e","i","o","u","A","E","I","O","U"]
l=[]
for i in d:
    if i in v:
        pass
    else:
        l.append(i)
d=l[::-1]
d="".join(d)
print(d)
