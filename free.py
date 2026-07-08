age = int(input("Enter your age: "))
if age == 0:
    print("Invalid age!")
elif age <= 13:
    print("Under age!")
elif age <= 18:
    print("You are a teenage!")
elif age <= 60:
    print("You are an adult!")
else:
    print("You are now a citizen!")
    
    
num = int(input("enter a number"))
print("=" * 20)
print("Table of " + str(num))
print("=" * 20)
for i in range (1, 13):
    print(str(num) + " x " + str(i) + " = " + str(num * i))
    

#ATM MACHINE
balance = 100000
while True:
    print("\n - ATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("choose an option")
    if choice == "1":
        print("BALANCE: N ", balance)
    elif choice == "2":
        amount = int(input("enter amount of deposit:"))
        balance += amount
        print("depodit successful")
        
    elif choice == "3":
        amount = int(input("enter your amount to withdraw"))
        if amount <= balance:
            balance -= amount
            print("Withdraw successful") 
        else:
            print("insufficent funds")  
            
    elif choice == "4":
        print("Thanks for using our ATM")
    break
else:
    print("Invalid option")    
                     
# password checker
correct_password = "python123"
password = input("enter your password")
if password == correct_password:
    print("Access granted")
else:
    print("Access denied")
    
# harder one in password checker
pin = "python123"
attempt = 3
while attempt >0:
    password = input("enter your password")
    if password == pin:
        print("Access Granted")
    elif attempt == 1:
        attempt -= 1
        print("wrong password")
        print("Account Locked")
    else:
        attempt -= 1
        print("wrong password")
        print("attempt left", attempt)
        
# shopping cart
item1 = input("enter your items")
price1 = float(input("enter your price"))
item2 =  input("enter item 2")
price2 = float(input("enter price"))
total = price1 + price2
print("\n _Reciept_")
print(item1, "$", price1)
print("item2", "$", price2)
print('=' * 30)
print("Total:", "$", total)

# contact book
contact = []
while True:
    print("\n _contact book_")
    print("1. add contact")
    print("2. view contact")
    print("3. search contact")
    print("4. exit")
    choice = input("choose an option")
    if choice == "1":
        name = input("enter contact name")
        phone = input("enter phone number")
        contact[name] = phone
        print("contact saved successful")
    elif choice == "2":
        for name, phone in contact. item():
            print(name, ":", phone)
    elif choice == 3:
        search = input("enter contact name:")
        if search in contact:
            print("phone number")
            
        else:
            print("contact not found")
    elif choice == "4":
        print("goodbye")
        break
    print("invalid option")                    
    
    # SIMPLE VOTING CHOICE
while True:
    print("\n===SIMPLE VOTING CHOICE===")
    print("A. APC")
    print("B. PDP")
    print("C. LP")
    choice = input("choose a party: ")
    if choice == "A":
        print("Candidate: Ahmend Tinubu") 
    elif choice == "B":
        print("Candidate: Peter Obi")     
    elif choice == "C":
        print("Candidate: Charls Soludu") 

    else:
        print("Candidate not found!")
        
        # GAMES
score = 0
print("welcome to quiz game:")
ans1 = input("what is the capital of Nigeria")
if ans1.lower() == " abuja ":
    print("correct!")
    score += 1
else:
    ("wrong!")
ans2 = input("how many days are in a week")
if ans2 == " 7 ":
    print("correcr!")
else:
    print("wrong!")
    
number = int(input(" enter number: "))
if number > 0:
    print(" positive! ")
elif number <= 0:
    print(" negative! ")
else:
    print("0")
    
# student register
student = []
name = input("enter student name: ")
age = input("enter age:")
student_class = input("enter your class: ")
school = {"name": name,
          "age": age,
          "class": student_class
          }
student.append(school)
print("\n ==student==")
for student in student:
    print(student)
    
# result checker
score = int(input("enter your score:"))
if score >= 80:
    print("Grade: A Execellent!")
elif score >= 70:
    print("Grade: B Very Good!")
elif score >= 60:
    print("Grade: C Good!")
elif score >= 40:
    print("Grade: D Fair!")
else:
    print("Grade: F Failed")