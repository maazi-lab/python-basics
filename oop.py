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

#  abstract class
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof"
    
dog = Dog()
dog.sound()

# another example of abstract class
from abc import ABC, abstractmethod
class appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class Tv(appliance):
    def turn_on(self):
        print("TV is turned on")

class Fan(appliance)
def turn_on(self):
        print("Fan is turned on")
        
tv = Tv()
fan = Fan()
tv.turn_on()
fan.turn_on()