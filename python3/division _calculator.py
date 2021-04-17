print ("Give me two numbers and I will divide them for you! ")
print("Type in 'q' to quit at anytime")

while True:
    x = input("Enter the first number: ")
    if x == 'q':
        break
    y = input("Enter the second number: ")
    if y == 'q':
        break
    try:
        answer = float(int(x) / int(y))
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero")
    break