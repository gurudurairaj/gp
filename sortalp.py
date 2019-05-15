a=int(input())
s=list(map(str,input().split()))
s.sort()
s.sort(key=len)
for i in range(len(s)):
    print(s[i].lower())
