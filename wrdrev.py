g=list(map(str,input().split()))
j=[]
for i in g:
    j.append(i[::-1])
print(*j)
