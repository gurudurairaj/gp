a=input()
c=[]
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
print("".join(c))
