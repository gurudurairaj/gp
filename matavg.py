a=int(input())
s=[]
sd=0
for i in range(a):
    s.append(list(map(int,input().split())))
for i in range(a):
    for j in range(a):
        sd=sd+s[i][j]
c=sd/(a*a)
        
    
print('%.6f'%c)
