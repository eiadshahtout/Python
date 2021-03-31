myPets = ["Lusie","Busie"]
print ("Enter your pet's name")
x = input()

if x not in myPets:
    print("I don't have a pet called " + x)
else:
    print("I have a pet called" + " " + x + " "+ "too")
