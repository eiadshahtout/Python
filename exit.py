import sys

def func2():
    print("1.Type a number ")
    print("2.Exit the program ")
    global response 
    response = int(input())
    

func2()

def func1():
        print('Are you sure ? ') 
        print("Yes or No")
        response = input()
        if response == 'Yes':
            sys.exit()
        elif response == "yes":
            sys.exit()
        else:
            func2()

if response == 1:
    secondresponse = input("Print a number ")
    print ("You typed in "+ secondresponse+ ".")
elif response == 2:
    func1()
