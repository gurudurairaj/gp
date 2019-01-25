n=int(input())
j=[]
su=0
mylist=list(map(int,input().split()))
for i in mylist:
    if int(i) <0:
        su=su+i
print(su)
