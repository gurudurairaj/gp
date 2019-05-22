a=input()
a=list(a)
i=0
while i<len(a):
    if a[i]==" " and a[i-1]==" ":
        del a[i]
        i=i-1
    i=i+1
print("".join(a))

