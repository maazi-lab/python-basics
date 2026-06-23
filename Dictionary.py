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
    
    
