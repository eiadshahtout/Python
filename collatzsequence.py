import sys

def collatz(number):
    if number % 2 == 0:           # Even number
        result = number // 2
    elif number % 2 == 1:         # Odd number
        result = 3 * number + 1

    while result == 1:            # It would not print the number 1 without this loop
        print(result)
        sys.exit()                # So 1 is not printed forever.

    while result != 1:            # Goes through this loop until the condition in the previous one is True.
        print(result)
        number = result           # This makes it so collatz() is called with the number it has previously evaluated down to.
        return collatz(number)    

print('Enter a number: ')         # Program starts here!
try:
    number = int(input())         # ERROR! if a text string or float is input.
    collatz(number)
except ValueError:
	print('You must enter an integer type.')

                                  # Fully working!