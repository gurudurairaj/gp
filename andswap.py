s=list(map(str,input().split()))
for i in range(len(s)):
    if len(s)==1:
        break
    if s[i]=="and":
        s[i-1],s[i+1]=s[i+1],s[i-1]
print(*s)
