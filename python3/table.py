people = input("How many people are you booking for? ")
people = int(people)

if people < 8:
    print("Your table is ready")
else:
    print("You have to wait for a table. Sorry!")