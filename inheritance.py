# Inheritance in OOP
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

#  Child one
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def barking(self):
        print(f"{self.name} Says: woof")
    
# Second Child
class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def meow(self):
        print(f"{self.name} Says: meow")
        
class Bird(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def fly(self):
        print(f"{self.name} Says tweet tweet")
        

dog = Dog("Bingo", 2, "German sheperd")
cat = Cat("Katty", 4, "White")
bird = Bird("Tweety", 1, "True")

dog.eat()
cat.eat()
bird.eat()

# Nigeria Bank Example
class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be more zero")
        self.balance += amount
        print(f"Deposited Amount: {amount} Naira")
        print(f"New Balance: {self.balance} Naira")
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount must be above zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdraw Amount: {amount} Naira")
        print(f"New Balance: {self.balance} Naira")
        
    def show_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance} Naira")
        
# child one
class Saving_account(Bank_account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest Added:{interest} Naira")
        print(f"New Balance: {self.balance} Naira")
        
    def show_info(self):
        super().show_info()
        print(f"Interest Rate: {self.interest_rate}%")

# Child two
class Current_account(Bank_account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def overdraft(self, amount):
        if amount > self.overdraft_limit:
            raise ValueError("Exceed limit")
        self.balance -= amount
        print(f"Overdraft of {amount} Naira Approved")
        print(f"New Balance {self.balance} Naira")
        
    def show_info(self):
        super().show_info()
        print(f"Overdraft: {self.overdraft_limit} Naira")
    
# child three
class StudentAccount(Bank_account):
    def __init__(self, owner, balance, school):
        super().__init__(owner, balance)
        self.school = school    

    def pay_school_fees(self, amount):   
        discount = amount * 0.1        
        final    = amount - discount
        if final > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= final
        print(f"School fees paid!")
        print(f"Discount: {discount} naira")
        print(f"Paid: {final} naira")
        print(f"Remaining balance: {self.balance} naira")

    def show_info(self):
        super().show_info()
        print(f"School: {self.school}")
        
# create accounts
savings = Saving_account("MyrakTech", 100000, 5)
current = Current_account("Echezona", 50000, 20000)
student = StudentAccount("Favour", 30000, "University of Lagos")

# ALL using INHERITED methods from BankAccount!
print("===== SAVINGS ACCOUNT =====")
savings.show_info()
savings.deposit(20000)       # ✅ inherited!
savings.withdraw(10000)     # ✅ inherited!
savings.add_interest()      # ✅ own method!

print("\n===== CURRENT ACCOUNT =====")
current.show_info()
current.deposit(10000)      # ✅ inherited!
current.withdraw(20000)     # ✅ inherited!
current.overdraft(5000)     # ✅ own method!

print("\n===== STUDENT ACCOUNT =====")
student.show_info()
student.deposit(50000)           # ✅ inherited!
student.pay_school_fees(5000)  # ✅ own method!
        
        
