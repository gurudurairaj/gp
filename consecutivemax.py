a=input()
c=1
s=0
g=""
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c=c+1
    if c>s:
        s=c
        g=a[i]
    if a[i]!=a[i+1]:
        c=1
print(g,s)
        
        
