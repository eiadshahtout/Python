import sys

print("1.Type a number ")
print("2.Exit the program ")
response = int(input(""))

def func1():
    while True:
        print('Are you sure ? ') 
        print("Yes or No")
        response = input()
        if response == 'Yes':
            sys.exit()
        elif response == "yes":
            sys.exit()

if response == 1:
    secondresponse = input("Print a number ")
    print ("You typed in "+ secondresponse+ ".")
elif response == 2:
    func1()
