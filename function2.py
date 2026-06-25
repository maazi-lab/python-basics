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

def greet():
    print("Hello student")
    
greet()

def greet(name):
    print("hello", name)
    
greet("john")
greet("amina")

def add(a, d):
    print(a + d)

add(5, 10)

def add(a, d):
    return a + d

result = add(10, 20)
print(result)

# argument in function
def numbers(* args):
    print(args)
    
numbers(1, 2, 3, 4, 5, 6, 7)

def add(*args):
    total = 0
    
    for num in args:
        total += num
        
    return total

print(add(2, 4, 7))

# def in kwargs
def student(**kwargs):
    print(kwargs)
    
    
student(name = "john", age = 15, level = "ss2")
    
# scope in function
x = 5 # global variable
def show():
    print(x)

show()

def show():
    x = 10 # local variable
    print(x)


# argument in function

def moni(*me):
    for item in me:
        print(item)
        
moni("john", "mary", "james", "favour")


def find_max(*args):
    return max(args)
print(find_max(2, 4, 6, 8, 10))


def display(*args):
    for item in args:
        print(item)

display("python", "java", "c++", "javascript")
display("apple", "banana", "cherry")

def profile(**kwargs):
    print(kwargs)

profile(name = "john", age = 20, country = "USA")

# args and kwargs in function
def info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    
info("python","jango", name = "john", age = 20)
# local and global variable
name = "global name"
def total():
    name = "local name"
    print(name)
    
total()
print(name)

# global keyword in function
count = 0


def increase():
    global count
    count += 1
    
increase()
print(count)

def register(**kwargs):
    print("User Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
register(name = "john", age = 20, email = "john@example.com")

try:
    print(10 / 2)
except:
    print("Error: Division by zero is not allowed.")
finally:
    print("Division successful.")
    
    
    