s=["a","e","i","o","u"]
d=input()
d=list(d)
f=""
g=""
for i in d:
    if i in s:
        f=f+i
    else:
        g=g+i
print(f+g)
