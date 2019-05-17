a=int(input())
s=list(map(int,input().split()))
d=[]
for i in range(len(s)-1):
    m=s[i+1:len(s)]
    m.sort(reverse=True)
    d.append(m[0])
d.append(0)
print(*d)
    
