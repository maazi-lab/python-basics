# advanced function
def add(*args):
    print(args)

add(5, 10)
add(20, 30, 3)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# add numbers using *args
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_numbers(5, 10))
print(add_numbers(20, 30, 3))
print(add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def student_record(**kwargs):
    print(kwargs)
    
student_record(name = "MyrakTech", age = 20, course = "AI")
store = ("rice", "beans", "yam", "plantain")
for item in store:
    print(item)
    
def store(**kwargs):
    print(kwargs, "items in the store")
    
kwargs = {"rice": 100, "beans": 200, "yam": 300, "plantain": 400}

def student_record(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print(student_record(name = "MyrakTech", age = 20, course = "Tech Academy"))

# scope in function
name = "MyrakTech"
def greet():
    # local variable
    message = "Hello, welcome to MyrakTech!" 
    print(message) #can access local variable inside the function
    print(name) # can access global variable inside the function
greet()
print(name) # can access global variable outside the function

counter = 0
def increase():
    global counter # declare counter as global to modify it
    counter += 1
    print("inside the function:", counter)
    
increase()
increase()
increase()
print("outside the function:", counter) # can access global variable outside the function

my_name = "MyrakTech"
def greet():
    welcome_message = f"Hello, {my_name}!" # local variable
    print(welcome_message) # can access local variable inside the function
    print(my_name) # can access global variable inside the function
greet()
print(my_name) # can access global variable outside the function

num = 34
def nums(a, b):
    sum = a + b
    print(f"adding number, {sum}")
    
nums(34, 67)
nums(16, 90)
nums(14, 34)
print(num)

score = (67, 45, 89, 90)
def total_scores():
    total = sum(score)
    print(f"Total: {total}")
    return total

def average_scores():
    total = total_scores()
    average = total / len(score)
    print(f"Average: {average}")

total_scores()
average_scores()
print(f"Score: {score}")

