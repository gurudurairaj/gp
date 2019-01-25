n=int(input())
j=[]
su=0
for i in range(n):
    j.append(int(input()))
for i in j:
    if i <0:
        su=su+i
print(su)
