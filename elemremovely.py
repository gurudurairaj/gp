a,b=map(int,input().split())
s=list(map(int,input().split()))
h=[]
for i in range(len(s)):
    if s[i]!=b:
        h.append(s[i])
print(h)
    
