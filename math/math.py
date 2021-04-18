import sys, time,cmath
from numpy import sqrt

def main():
    print("-" * 50)
    print("Welcome to the Math Calculator! ")
    time.sleep(0.2)
    print("\npress q to quit at any time ")
    print("-" * 50)
    if True:
        start()

def start():
    print("\n Choose an option: ")
    print("1. Quadratic Formula Calculator")
    print("-" * 50)
    response = input()
    if response == "1":
        quadratic_formula()
    elif response == "q":
        sys.exit()

def quadratic_formula():
    a=float(input("a ="))
    b=float(input("b ="))
    c=float(input("c ="))
    if a==0:
        print("What the what?? This is not a quadratic equation.")
        b=0
        c=0
        a=1
        
        
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print("x1 = "+str(x1))
    print("x2 = "+str(x2))

if __name__ == "__main__":
    main() 