fa=input()
c=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
if fa=="a" or  fa=="e" or  fa=="i" or  fa=="o" or fa=="u":
    print("Vowel")
elif fa in c:
    print("Consonant")
else:
    print("invalid")
