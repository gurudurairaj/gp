a=input()
h=[]
for i in range(len(a)):
    if a[i] not in h:
        h.append(a[i])
h.sort(reverse=True)
print("".join(h))
    
