try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("program finished.")
    
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: please enter a valid number.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("program finished.")
    
try:
    print(10 / 0)
except:
    print("An error occurred.")
print("i'm still running")


def buy_item(price_item):
    try:
        price = int(price_item)
        print(f"The price of the item is: {price}")
    except ValueError:
        print("Error: please enter a valid number for the price.")
        
buy_item("5000") # Output: The price of the item is: 5000
buy_item("plenty") # Output: Error: please enter a valid number for the price.

try:
    price = ("5000")
    print(int(price))
except ValueError:
    print("Error: please enter a valid number for the price.")
else:
    print("No error found")
print("program finished.")

def names(names_list):
    try:
        print(names_list[10])
    except IndexError:
        print("Error: index out of range.")
    else:
        print("No error found")
print("program finished.")
names(["Peter", "John", "Mary"]) # Output: Error: index out of range.

def works(hand_works):
    try:
        for work in hand_works:
            print(monitor)
    except NameError:
        print("Error: variable 'monitor' is not defined.")
    else:
        print("No error found")
print("NO ISSUES")
works(["painting", "drawing", "sculpting"]) # Output: Error: variable 'monitor' is not defined. 
    
# final and raise
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    print(f"Withdrawing {amount} from the account.")
    
try:
    withdraw(-500)
except ValueError as e:
    print("GTB says:", e)
finally:
    print("Transaction completed.")
    
# custom exception
# create a custom exception class called InsufficientFundsError that inherits from the built-in Exception class. This exception will be raised when a withdrawal amount exceeds the available balance in a bank account.
class InsufficientFundsError(Exception):
    pass
# use the custom error.
def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds in the account.")
    print(f"Withdrawing {amount} from the account.")

# catch the custom error
try:
    withdraw(1500, 1000)
except InsufficientFundsError as e:
    print("GTB says:", e)
    
# school error
class SchoolFeeError(Exception):
    pass
def pay_school_fee(amount):
    if amount < 50000:
        raise SchoolFeeError("School fee must be at least 50,000.")
    print(f"Payment of {amount} received for school fee.")
    
try:
    pay_school_fee(20000)
except SchoolFeeError as e:
    print("UNIQUE SECONDARY SCHOOL says:", e)
finally:
    print("Vsit us again.")
    
