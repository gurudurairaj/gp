a=input()
l=[]
i=0
j=0
v=""
g=[]
while i<(len(a)):
    if a[i].isalpha():
        l.append(a[i])
    elif a[i].isdigit():
        v=v+a[i]
        j=i+1
        if j==len(a):
            l.append(v)
            v=""
        while j<len(a):
            if a[j].isdigit() and j==len(a)-1:
                v=v+a[j]
                l.append(v)
                v=""
                j=100
                break
            elif a[j].isalpha() or j==len(a)-1:
                l.append(v)
                v=""
                break
            elif a[j].isdigit() :
                v=v+a[j]
                print(v)
            j=j+1
        i=j-1
    i=i+1
for i in range(len(l)):
    if l[i].isalpha():
        g.append(l[i])
    elif l[i].isdigit():
        m=int(l[i])
        if m%2!=0:
            g.append(l[i])
        else:
            for x in range(int(l[i])-1):
                g.insert(len(g)-1,l[i-1])
print("".join(g))
