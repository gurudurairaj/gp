n=int(input())
h=list(map(int,input().split()))
k=[]
i=min(h)
j=max(h)
i=h.index(i)
j=h.index(j)
k.append(i+1)
k.append(j+1)

print(*k)
