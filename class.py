states = ["Ebonyi", "Enugu", "Anambra", "Kaduna", "Imo"]
print(states[0])
print(states[4])

num = [3, 45, 6, 8, 9]
for nums in num:
    print(sum(num))
    
animal = ["goat", "sheep", "bird", "lion", "horse"]
for i in animal:
    print(i)
    
num  = [23, 40, 10, 10, 17, 15]
for number in num:
    if number >= 15:
        print(number)
        
fruits = ["apple", "mango", "orange", "guava", "pineapple"]
fruits.append("watremelom")
fruits.remove("orange")
print(fruits)

student_score = [45, 78, 85, 96, 74, 88]
highest = max(student_score)
print("HIGHEST SCORE: ", highest)

NUM = [16, 4, 8, 9, 7, 5, 11, 10]
for i in num:
    if i % 2 == 0:
        print("even")
        
names = ["Ngozi", "John", "Favour", "Emeka", "Echezona"]
names.sort()
print(names)

num = [89, 50, 45, 66, 78, 88, 99, 77, 34, 44]
count = 0
for i in num:
    if i > 50:
        print(i)
        count += 1
        
student = ["emeka", "joy", "john", "echezona", "favour"]
score = [67, 78, 88, 79, 65]
                                                   
for i in range (len(student)):
    print(student[i] +  " : " + str(score[i]))            
    
words = ["money", "egg", "life", "honey", "heavy"]
for word in words:
    if len(word) > 4:
        print(word)                                                                                             
        
number = []
for i in range(1, 11):
    number.append(i)
    print(number)