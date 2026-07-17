# File: assignment.py
# Demonstrates string operations, list and dictionary use, and basic input/output.

name = input("enter your name: ")
name.upper()
print(name)
print(name.title())
sent = input("make a sentence: ")
print(sent.lower())
print(sent.capitalize())
sent1 = ("i have a dog!")
sent1.replace("dog", "cat")
print(sent1)
print(sent1.count("a"))

word = "principle"
print(word.startswith("p"))
print(word.endswith("le"))

fruit = " mango  money   "
print(fruit.split())

fruit = ["mango", "apple", "orange"]
result = "-".join(fruit)
print(result)

# dictionary
student = {"name": "echezona",
           "age": 20,
           "student_class": "ss3B"
           }
print(student)

students = {"name": "echezona",
            "age": 20,
            "school": "University of Nigeria",
            "course": "Machine Learning"
            }
print(students["age"])
print(students.keys())

subject = {"English": 75,
           "Maths": 67,
           "Economics": 89
           }
print(subject)


product = {"Rice": 3500,
           "Beans": 4000,
           "Garri": 2500,
           "Fish": 6000
           }
for product, price in product.items():
    print(product + ":  N" + str(price))
    

# coditions in dictionary
username = input("enter your username! ")
if username == "Admin":
    print("Welcome!!")
else:
    print("Not Welcomed!!")

country = {"Nigeria": "Abuja",
           "UK": "Ukrain",
           "Ghana": "Congo"
           }
print(country.values())
     

student = {"emeka": 67,
           "joy": 90,
           "favour": 88,
           "mary": 77
           }
name = input("enter your name:")
if name in student:
    print("score" + " : " + str(student[name]))
else:
    print("name not found!!")

fruits = {"mango": 400,
          "apple": 600,
          "orange": 500,
          "guava": 700
          }
fruit = input("enter fruit name: ")
if fruit in fruits:
    print("price: " + "N" + str(fruits[fruit]))
    
course = {"English": 15000,
         "Maths": 12000,
         "Literature": 20000,
         "Igbo": 18000
         }
courses = input("enter your course")
if courses in course:
    print(str(course[courses]))
    

# project student resuit checker:

student = {"Echezona": 84,
           "Favour": 57,
           "John": 70,
           "Joy": 64
           }
name = input("enter your name: ")
if name in student:
    print("name found!!")
else:
    print("name not found!!")
score = student[name]
if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
    
print("Name: " + name)
print("Score: " + str(score))
print("Grade: " + grade)
if score > 80:
    print("Remark: Execellent!")
elif score > 70:
    print("Remark: Very Good!")
elif score > 60:
    print("Remark: Good!")
elif score > 50:
    print("Remark: Average!")
else:
    print("Remark: Failed!")
    

