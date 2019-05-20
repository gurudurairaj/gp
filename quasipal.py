n=input()
if n==n[::-1]:
    print("yes")
else:
    h="00"+n
    i=n+"00"
    if h==h[::-1]:
        print("yes")
    elif i==i[::-1]:
        print("yes")
    else:
        print("no")
