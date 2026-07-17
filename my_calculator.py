# File: my_calculator.py
# Demonstrates a command-line calculator application using basic arithmetic operations.

import math
while True:
    print("=====MYRAKTECH CALCULATOR====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Moduous - Remainder")
    print("7. Power \ Exponent")
    print("8. Square Root")
    choice = input("enter your operation (1, 8): ")
    if choice == "8":
        num1 = float(input("enter one number: "))
    else:
        num1 = float(input("enter second number: "))
        num2 = float(input("enter first number: "))
    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}") 
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 == 0:
            print("Error! cannot divide by zero! ")   
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    elif choice == "5":
        result = num1 // num2
        print(f"{num1} // {num2} + {result}")
    elif choice == "6":
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    elif choice == "7":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")
    elif choice == "8":
        result == math.sqrt(num1) 
        print(f"Square Root of {num1} = {result}") 
    else:
        print("Invalid Operation!") 
        again = input("Caculate again! (Yes, No):")
        if again.lower() != "yes":
            print("Thank you for using MYRAKYECH CALCULATOR!!")
            break     

            