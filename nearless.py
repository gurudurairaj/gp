a=int(input())
s=list(map(int,input().split()))
l=[]
for i in range(a-1):
    if s[i]>s[i+1]:
        l.append(s[i+1])
    else:
        l.append(-1)
l.append(-1)
print(*l)
        
