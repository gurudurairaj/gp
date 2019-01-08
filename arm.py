n=input()
q=0
k=0
for i in range(1,len(n)+1):
    s=int(n[q :i])
    k=k+(s*s*s)
    q=q+1
if k==int(n):
    print("yes")
else:
    print("no")
