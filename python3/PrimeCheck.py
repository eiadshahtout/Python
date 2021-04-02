# This is to find if it's a prime number
import math
def primeCheck(number):
    if number % 2 == 0 and number > 2: 
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))

def main():
    print(primeCheck(3997))
    print(primeCheck(100))
    print(primeCheck(77))

if __name__ == '__main__':
	main()
