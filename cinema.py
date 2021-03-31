import sys

prompt = "\nPlease enter your age:"
prompt += "\n(Enter '00' when you are finished.) "

price = True
while price:
    age = int(input(prompt))
    
    if age >= 0 and age <= 3:
        print("The ticket is free!")
    elif age >= 3 and age <= 12:
        print("Your ticket price is $10")
    elif age <= -1:
        print("Invalid age try again!")
    else:
        print("Your ticket price is $15")
    
    if age == 00:
        break