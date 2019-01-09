n=int(input())
s=[]
for i in range(n):
    s.append(input())
s.sort(reverse=True)
print("".join(s))
