# File: oop.py
# Demonstrates object-oriented programming with classes and methods.

class Student:
    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class

student1 = Student("John Doe", 20, "10th Grade")
student2 = Student("Jane Smith", 19, "11th Grade")

print(f"Student 1: {student1.name}, Age: {student1.age}, Class: {student1.student_class}")
print(f"Student 2: {student2.name}, Age: {student2.age}, Class: {student2.student_class}")

# create a class of phone with attributes of brand, model, price and methods to display the details of the phone and to apply a discount on the price of the phone. Create two instances of the class and display
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def make_call(self, number):
        print(f"Making a call to {number} using {self.brand} {self.model}.")
        
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")    

# create student class 
phone1 = Phone("Apple", "iPhone 13", 50000)

phone1.make_call("123-456-7890")
phone1.show_info()
# business type 
class business:
    def __init__(self, name, capital, location):
        self.name = name
        self.capital = capital
        self.location = location
    def business_name(self, name):
        print(f"The name of my business is {name}")
    def my_capital(self, capital):
        print("I started my business with {capital}")
    def my_location(self, location):
        print(f"I stay at {location}")
        
business1 = business("fish business", 500000, "Lagos state")
business1.business_name("Fish business")
business1.my_capital(500000)
business1.my_location("Lagos state")


# ecaspulation in OOP
class bank_account:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance
        self.__pin = pin
    
# createb account
account = bank_account("MyrakTech", 50000, "maazi17081426")
# try to print it directly
#print(account.__balance)
#print(account.__pin) WRONG!

# how to read the private code using getter
class bankAccount:
    def __init__(self, pin, balance, owner):
        self.__pin = pin
        self.__balance = balance
        self.__owner = owner
        
    def get_balance(self):
        return self.__balance

account = bankAccount("17081426mid", 50000, "MyrakTech")

print(account.get_balance())  

class score:
    def __init__(self, student, score, grade):
        self.student = student
        self.__score = score
        self.__grade = grade
    def get_score(self):
        return self.__score
    
    def get_grade(self):
        return self.__grade
    
scores = score("Echezona", 76, "A1")

print("Echezona")
print("Student score: ", scores.get_score())
print("Student grade: ", scores.get_grade())
        
class MTNbundle:
    def __init__(self, phone_number, data_balance, pin):
        self.phone_number = phone_number
        self.__data_balance = data_balance
        self.__pin = pin
        
    def get_data_balance(self):
        return self.__data_balance  
       
    def buy_data(self, amount_gb):
        if amount_gb <= 0:
            raise ValueError("amount must not be less than or equal to zero")
        if amount_gb > 100:
            raise ValueError("maxi,um bundele is 100gb")
        self.__data_balance += amount_gb
        print(f"Successfully added {amount_gb}GB!")
        print(f"New balance: {self.__data_balance}GB")
        
    def use_data(self, amount_gb):
        if amount_gb < 0:
            raise ValueError("amount must not be less o")
        if amount_gb > self.__data_balance:
            raise ValueError("not enpough balance") 
        self.__data_balance -= amount_gb
        print(f"used data: {amount_gb}")
        print(f"remaining data: {self.__data_balance}")
        
    def show_info(self):
        print("\n account info")
        print(f"\n Phone numbe: {self.phone_number}")
        print(f"\n Data balance: {self.__data_balance} gb")
        print(f"\n Pin! *****Hidden****")
        

mtn = MTNbundle("08030523592", 5, 1234)

mtn.show_info()
mtn.buy_data(10)
mtn.use_data(7)
print(" FINAL BALANCE")
print(f"Final balance: {mtn.get_data_balance()}" )

# HOSPITAL RECORD!!

class hospitalpatient:
    def __init__(self, name, medical_record, medical_prescription):
        self.name = name
        self.__medical_record = medical_record
        self.__medical_prescription = medical_prescription

    def get_medical_record(self):
        return self.__medical_record
    
    def get_medical_perscription(self):
        return self.__medical_prescription
    
    def update_medical_record(self, new_record):
        if not isinstance(new_record, str):
            raise TypeError("medical record musy text!")
        if len(new_record) < 5:
            raise ValueError("new record must be more than five characters")
        self.__medical_record = new_record
        print("Record Updated!")
        print(f"New record: {self.get_medical_record}")
        
    def update_medical_prescription(self,new_perscription):
        if not isinstance(new_perscription, str):
            raise TabError("perscription must be in text")
        if len(new_perscription) < 3:
            raise ValueError("perscription is too short")
        self.__medical_prescription = new_perscription
        print("Perscription Updated")
        print("New perscription {elf.__medical_prescription}")
    
    def show_info(self):
        print(f"\n Patient name: {self.name}")
        print(f"\n Medical record: {self.__medical_record}")
        print(f"\n Perscription: {self.__medical_prescription}")

patient = hospitalpatient("Fvour", "maliaria", "Coartem 3 times daily")

patient.show_info()
print("\n  Reading Record!")
print(patient.get_medical_record())
print(patient.get_medical_perscription())

print("\n ----Doctors New Record----")
patient.update_medical_record("Malaria and Typhoid fever")
patient.update_medical_prescription("Coartem and Ciprofloxacin")
print("\n--- trying direct access ---")
print("\n--- final info ---")
patient.show_info()