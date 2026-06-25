student = {"name": "john",
           "age": 20,
           "class": "ss2"
           }

print(student["name"])
# uptade in dictionary adding
student["school"] = "Ben scondary school"
print(student)
# changing in dictionary
student["age"] = 17
print(student)
# removing informatio
del student["class"]
print(student)
# input and output in dictionary
name = input("enter name:")
age = input("entr your age:")
students = {"name":  name,
           "age": age
           }
print(students)
# dictionary with arithematics
score = {"math": 70,
         "english": 80,
         "biology": 90
         }
total = score["biology"] + score["english"] + score["math"]
print("total = ", total)
# dictionary with condition 

scores = {"math": 70,
          "english":  80,
          "biology": 90
          }
if "english" in score:
    print("english found")
else:
    print("not found")
    

# loop with dictionary printin only the keys
grade = {"math": 50,
         "english": 70,
         "igbo": 79
         }
for key in grade:
    print(key)
# printing key and value using loop in dictionary
for key, value in grade.items():
    print(key, "=", value)
    
# while loop in dictionary
score = {"maths": 70,
         "english": 80,
         "igbo": 97
         }
keys = list(score.keys())
i = 0
while i < len(keys):
    print(keys[i], "=", score[keys[i]])
    i += 1
    

# building student record
student = {}
student["name"] = input("enter your name:")
student["age"] = input("enter your age:")
student["class"] = input("enter your class")
print("\student record")
print(student)

# dictionary challenge

mine_record = {"name" = "john",
               "age" = 20,
               "class" = "ss2"
               }
print("my record")    


phone = {"brand": "samsung",
        "price": 200000,
        "color": "black"
        }

print(phone)

countries = {"nigeria": "lagos",
                "ghana": "accra",
                "kenya": "nairobi"
                }
for key, value in countries.items():
    print(key, "=", value)

# Create student dictionary, update age, add grade, and print
student = {"name": "John", "age": 20, "class": "SS2"}
print("Original dictionary:", student)

# Update age value
student["age"] = 21
print("After updating age:", student)

# Add new key "grade"
student["grade"] = "A"
print("Full dictionary with grade:", student)

student_score = {"emeka": 85, "ngozi": 90, "mary": 78, "favour": 92, "andrew": 88}
for name, score in student_score.items():
    print(f"{name}: {score}")
    
students = {"emeka": 85, "ngozi": 90, "mary": 78, "favour": 92, "andrew": 88}
for name, score in students.items():
    print(max(students, key=students.get))

# Shop dictionary with name, location, and list of products
shop = {
    "name": "Tech Store",
    "location": "Main Street",
    "products": ["Laptop", "Phone", "Headphones", "Charger", "USB Cable"]
}

print("Shop Name:", shop["name"])
print("Products in", shop["name"] + ":")
for product in shop["products"]:
    print("  -", product)

# Mini Dictionary - Words and their meanings
word_meanings = {
    "python": "A high-level programming language known for simplicity",
    "algorithm": "A step-by-step procedure for solving a problem",
    "variable": "A named storage location that holds a value",
    "function": "A reusable block of code that performs a specific task"
}

# Ask user to enter a word
user_word = input("Enter a word to find its meaning: ").lower()

# Check if word exists in dictionary and print meaning
if user_word in word_meanings:
    print("Meaning:", word_meanings[user_word])
else:
    print("Word not found in dictionary!")
    


