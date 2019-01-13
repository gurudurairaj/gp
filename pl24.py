f=input()
c=0
for i in f:
    if i.isdigit():
        c=c+1
if c==len(f):
    print("yes")
else:
    print("no")
