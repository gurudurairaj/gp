a=input()
l=[]
for i in range(len(a)):
    if a[i] not in l:
        l.append(a[i])
print("".join(l))
    
