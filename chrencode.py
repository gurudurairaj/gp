s=input()
s=list(s)
a=[]
for i in s:
    if i=="x":
        a.append("a")
    elif i=="y":
        a.append("b")
    elif i=="z":
        a.append("c")
    elif i=="X":
        a.append("A")
    elif i=="Y":
        a.append("B")
    elif i=="Z":
        a.append("C")
    else:
        c=ord(i)
        a.append(chr(c+3))
print("".join(a))
