def greet():
    print("welcome to myraktech")
    
greet()

def print_name():
    print(" echezona " * 5)

print_name()

def num(a, b):
    result = a + b
    return result

ans = num(12, 64)
print(str(ans))

def is_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
         

is_age(13)
is_age(67)

def mutiply(a, b):
    result = a * b
    return result

ans = mutiply(67, 90)
print("answer: ", ans)

def biggest(a, b, c):
    return max(a, b, c)

print(biggest(34, 45, 78))

def count_word(word):
    return len(word)

print(count_word("echezona"))
print(count_word("mary"))

def greeting(name, greeting = "Hello"):
    print(greeting + " " + name + "!")
    
    
greeting("Echezona", "Welcome")
greeting("Danie", "Godd Morning")
greeting("John")

def num(a, b,  c, d, e):
    number = (a, b, c, d, e)
    for nums in number:
        if nums % 2 == 0:
            print("Number: Even!")
        else:
            print("Number: Odd!")
            

num(2, 4, 9, 8, 7)


def calculator_grade(score):
    if score >= 70:
        print("GRADE: A")
    elif score >= 60:
        print("GRADE: B")
    elif score >= 50:
        print("GRADE: C")
    else:
        print("FAILED!")
    

calculator_grade(56)

def print_many(word, time):
    for i in range(time):
        print(word)
    
print_many("Echezona", 5)
print("=" * 10)
print_many("Fvour", 6)
print("=" * 10)
print_many("Beautiful", 3)

def full_intro(name, age, course):
    print(f"my name is {name}, i am {age}, years old, im in {course}")
    
    
full_intro("Miracle", "17", "Tech")
