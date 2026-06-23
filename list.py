state = ["Ebonyi", "Enugu", "kogi", "kano", "Delta"]
print(state)
# print one in list
states = ["Lagos", "Kano", "Rivers", "Abuja", "oyo"]
print(states[0])
print(states[4])
# remove and replace
fruits = ["apple", "mango", "orange", "pineapple", "grape"]
fruits.remove("orange")
fruits[2] = "watermelon"
print(fruits)
# adding in items in list
subject = []
subject.append("economics")
subject.append("english")
subject.append("maths")
subject.append("literatue")
print(subject)
# insert in list
colours = ["red", "blue", "green"]
colours.insert(2, "yellow")
print(colours)
# remove in list
animal = ["dog", "cat", "goat", "lion"]
animal.remove("goat")
print(animal)
# remove or numbers with  pop in list
num = [ 2, 3, 4, 5, 6, 7]
remove = num.pop(3)
print("removed item:", remove)
print("updaated item:", num)

#  len in list
students = ["emeka", "john", "luke", "nogozi", "favour", "miracle", "faih", "ebuka"]
print(len(students))

# condition in list
food = ["rice", "indomie", "yam", "speghetti"]
if "beans" in food:
    print("item found")
else:
    print("not found")

# for loop in list
countries = ["Nigeria", "Ghana", 'Kenya', "USA", "Canada"]
for country in countries:
    print(country[3])
    print(country)
# string in list/ in uppercase
names = ["john", "emeka", "philip", "ngozi"]
for name in names:
    print(name.upper())
    
# in even numbers using while loop in list
number = [5, 10, 15, 20 , 25, 30]
i = 0
while i < len(number):
    print(number[i])
    i += 2
    
number = [5, 10, 15, 20 , 25, 30]
i = 1
while i < len(number):
    print(number[i])
    i += 2

# find the middle
students = ["john", "luke", "mary", "mathew", "favour"]
print(students[2])

# adding of numbers in list
num = [45, 60, 70, 85, 90]
total = sum(num)
print("Tota: l", total)
    
score = [45, 60, 70, 85, 68, 90]
total = sum(score)
average = total / len(score)
print("Total: ", total)
print("Average: ", average)

# adding in list
cart = []
cart.append("book")
cart.append("pen")
cart.append("pencil")
cart.append("bag")
cart.remove("pen")
cart.remove("book")
cart.append("sucks")
cart.append("text book")
print(cart)
# longest number and lowerst number
numbers = [12, 45, 7, 89, 34]
print(max(numbers))
print(min(numbers))

# remove and replace
students = ["john", "luke", "mary", "mathew", "favour"]
students.remove("luke")
students[2] = "andrew"
print(students)
#print(len(students))


# challenge for me
fruit = ["mango", "apple", "orange", "grape","tomato"]
print(fruit[2])

num = [4, 7, 9, 6, 7, 9]
for nums in num:
    number = sum(nums)
    print(str(number))
    
animal = ["goat", "sheep", ";oin", "monkey", "bird"]
for animals in animal:
    print(animals)
    
number = [17, 10, 65, 42, 5, 18]
for num in number:
    if num >= 15:
        print(num)

fruits = ["mango", "apple", "orange", "grape", "tomates"]
fruits.remove("orange")
fruits.append("guava")
print(fruits)

score = [56, 78, 90, 15, 57]
print("John highest: " + str(max(score)))


num1 = [4, 8, 7, 9, 6, 10]
for num in num1:
    if num % 2 == 2:
        print(num)
        
name = ["ifeoma", "miraclre", "joy", "echezona", "favour"]
print(name.sort())


number = [56, 45, 78, 56, 88, 99, 77, 90, 76, 74]
count = 0
for num in number:
    if num > 50:
        count += 1
print("count: ", count)


student = ["emeka", "joy", "ngozi", "ifeoma", "mmesoma", "monica"]
score = [85, 89, 67, 90, 56, 89]
for i in range(student, score):
    print(i(student), " : ", i(score))

words = ["mother", "love", "credit", "meat", "money"]
for word in words:
    if len(word) > 4:
        print(word)

num2 = []
for i in range(1, 11):
    num2.append()
    print(num2)