# student management system
class student_manager:
    def __init__(self, name, age, course, grade):
        self.name = name
        self.__age = age
        self.__course = course
        self.__grade = grade
    @property
    def get_age(self):
        return self.__age
    
    @property
    def get_course(self):
        return self.__course
    
    @property
    def get_grade(self):
        return self.__grade
    
    def update_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError("age must be an int")
        self.__age = new_age
        if new_age < 18:
            raise ValueError("Age must be at least 18")
        print("\n Age Updated!!")
        print(f"\n New age: {self.__age}")
        
    def update_course(self, new_course):
        if not isinstance(new_course, str):
            raise TypeError("Course must be in text")
        if len(new_course) <= 0:
            raise ValueError("course type not allowed")
        self.__course = new_course
        print("\n Course Updated!!")
        print(f"\n New Course: {self.__course}")
        
    def course_grade(self, grades):
        if not isinstance(grades, int):
            raise TypeError("grade must be a number")
        if grades >= 50:
            print(f"Grade A EXCELLENT!!: {grades}")
        else:
            print(f"Grade F FAILED: {grades}")
            
    def show_info(self):
        print("\n----Student Info---")
        print(f"\n Student Name: {self.name}")
        print(f"\n Student age: {self.__age}")
        print(f"\n Course: {self.__course}")
        print(f"\n Student Grade: {self.__grade}")

Student = student_manager("Echezona", 20, "Mathematics", 75)

Student.show_info()
print("\n ----STUDENT MANAGEMENT SYSTEM----")
print(Student.get_age)
print(Student.get_course)
print(Student.get_grade)

print("\n STUDENT UPDATED VERSION")
Student.update_age(20)
Student.update_course("mathematics and English")
Student.course_grade(75)
Student.show_info()

# Inheritance in OOP
class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

#  Child one
class dog(animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def barking(self):
        print(f"{self.name} Says: woof")
    
# Second Child
class cat(animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def meow(self):
        print(f"{self.name} Says: meow")
        
class bird(animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def fly(self):
        print(f"{self.name} is flying")