fruit = ("apple", "banana", "guava")
print(fruit)
print(fruit[-1])
# len of numbers
num = (10, 20, 30, 40, 50)
print(len(num))
#loops in tuples
fruit = ("aplle", "banana", "guava")
for fruits in fruit:
    print(fruit)
    print(fruit[0])
    
#conditional in tuples
fruit = ("apple", "banan", "guava")
if "banan" in fruit:
    print("found")
else:
    print("not found")
    
# adding in of nunbers in tuples
num = (5, 10, 15, 20)
print(sum(num))
# counting in tuples
num = (1, 2, 2, 2, 3)
print(num.count(2))

# finding position of an item
fruit = ("appe", "banana", "guava")
print(fruit.index("banana"))
print(fruit.index("guava"))
# input and output tonfind positiion
subject = ("maths", "english", "biology", "chemstry")
position = int(input("enter index(0-3):"))
print("subject: ", subject[position])
# tuple plus arithmatics
score = (70, 80, 90, 60, 100)
total = sum(score)
average = total / len(score)
print("Total: ", total)
print("Average: ", average)
# input and condition
fruit = ("apple", "banana", "orange")
fruits = input("enter your fruit:")
if fruits in fruit:
    print("found")
else:
    print("not found")
    
# for loops and tuple
fruits = ("apple", "banana", "orange")
for fruit in fruits:
    print(fruit)
    print(fruit[1])
# while loops in tuples
fruits = ("apple", "banana", "orange")
i = 0
while i < len(fruits):
    print(i)
    i += 1
    
scores = (25, 60, 45, 80, 90)
for score in scores:
    if score > 50:
        print(score)
        
number = (5, 10, 15, 20)
i = 0
total = 0
while i < len(number):
    total = total + number[i]
    i += 1
    print("Total: ", total)
    
# aassignment on tuple
fruit = ("apple", "mango", "guava", "banana", "pineapple")
print(fruit[0])

num (20, 30, 40, 50)
print(num-1)

name = ("john", "ngozi", "mary")
print(name)

colour1 = input("enter your colour:")
colour2 = input("enter your colour")
colour3 = input("enter your colour")
colours = (colour1, colour2, colour3)
print(colours)

num1 = int(input("enter number"))
num2 = int(input("enter number"))
num = (num1, num2)
print(num)

stud1 = input("what is your name")
stud2 = input("what is you name")
stud3 = input("what is your name")
stud4 = input("what is ypour name")
student = (stud1, stud2, stud3, stud4)
print(student)

num = (5, 10, 15)
print(sum(num))

num = (2, 4, 6, 8)
product = num[0] * num[1] * num[2] * num[3]
print("Product: ", str(product))

num = (100, 50)
different = num[0] - num[1]
print("diferent: ", str(different))

num = (5, 10, 15)
if 10 in num:
    print("number found")
else:
    print("number not found")

fruit = ("mango", "orange", "guava", "grape")
if "apple" in fruit:
    print("found")
else:
    print("not found")
    
cart = ("pen", "pencil", "book", "shirt")
lenght = len(cart)
if lenght >= 3:
    print("large tuple")
else:
    print("small tuple") 
    
num = (2, 4, 6, 8, 10) 
for nums in num:
    print(nums) 
    
num = (2. 4. 6, 8, 10) 
for nums in num:
    print(nums * 2)
    
name = ("emeka", "joy", "john","favour") 
for names in name:
    print(names.upper())
    
numbers = (10, 20, 30, 40, 50) 
i = 0
while i <= len(numbers):
    print(numbers[i])
    i = i + 1 
    
fruit = ("apple", "mango","grape", "banana","pineapple")
i = 0
count = 10
while i < len(fruit):
    count = count + 1
    i = i + 1
print("total of fruit:", str(count))
# print in reverse using while loop in tuple

numbers = (1, 2, 3, 4, 5, 6)
i = len(numbers) -1
while i >= 0:
    print(numbers[i])
    i = i - 1

# printing numbers greater 
num = (12, 4, 65, 8, 42)
for nums in num:
    if nums > 10:
        print(nums)
# average and input
num1 = int(input("enter number:")) 
num2 = int(input("enter number:"))
num3 = int(input("entre number:"))
number = num1 + num2 + num3
average = number / len(number)   

# find the largest number in tuple
number = (23, 45, 67, 85, 89, 95)
largest = number[0]
for num in number:
    if num  > largest:
        largest = num
        print("largest number", str(largest))
        
# check if all number are even number
num = (2, 4, 6, 8, 10)
all_even = True        
for nums in num:
    if num % 2 ! = 0:
        all_even = False
if all_even:
    print("all are number are even")
else:
    print("not all number are even")

# challenge for in python by clude:

colour = ("yellow", "blue", "black", "white", "pink")
print([2])

country = ("nigeria", "ghana", "congo", "egpt")
for countrys in country:
    print(countrys)
    
num = (4, 5, 6, 7, 8, 9)
print(num[5])
print(num[3])
  
career = ("echezoma", 19, "ML")
print(career[0])
print(career[1])
print(career[2])

num = (7, 8, 9, 6, 11, 5)
for nums in num:
    if nums % 2 != 0:
        print("odds", nums)
        
