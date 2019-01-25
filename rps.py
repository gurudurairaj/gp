a,b=input().split()
if a=="S" and b=="P" or a=="P" and b=="S":
    print("S")
if a=="R" and b=="S" or a=="S" and b=="R":
    print("R")
if a=="R" and b=="P" or a=="P" and b=="R":
    print("P")
