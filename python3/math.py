# Simple Calculator

def calculate(x,y,operator):
    if operator == "*":
        result = float(x * y)
        print(f"The answer is {result} ")
    elif operator == "/":
        result = float(x / y)
        print(f"The answer is {result} ")
    elif operator == "+":
        result = float(x + y)
        print(f"The answer is {result} ")
    elif operator == "-":
        result = float(x - y)
        print(f"The answer is {result} ")
    else:
        print("Try Again")

x = int(input("Enter First Number: \n"))
y = int(input("Enter Second Number: \n"))
operator = (input("What do we do with these? \n"))
calculate(x,y,operator)

