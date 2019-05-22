n=int(input())
m=list(map(int,input().split()))
c=0
for i in range(len(m)):
    for j in range(i,len(m)):
        if m[i]+m[j]==0 m[i]+m[j]==1:
            print(m[i],m[j])
            c=c+1
            break
    if c==1:
        break
