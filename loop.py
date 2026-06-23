for i in range (1, 21):
    print(i)
    
num = 6
for i in range (1, 11):
    print(str(num), " x ", str(i), "=", str(num * i))
    
for i in range (2, 30):
    num = i % 2
    if num == 0:
        print(i)
        
name = "myraktech"
for names in name:
    print(names[0])
    
for i in range (1, 31):
    num = i % 2
    num1 = i % 3
    if num == 0 and num1 == 0:
        print(i)
    
for i in range (1, 6):
    print('*' * i) 
    
    
day =  ("monday", "tuesday", "wensday", "thursday", "friday", "saturday", "sunday")
for days in day:
    if len(days) > 6:
        print(days)

for i in range (50, 0, -1):
    print(i)
    
for i in range (1, 5):
    for j in range (1, 5):
        print(i * j, end="\t")
    print()
    
num = [5, 12, 3, 18, 7, 25, 9, 14]
for i in num:
    if i > 10:
        print(i, end="\t")
    
    
sen = "artificial intelligent"
count = 0
for car in sen.lower():
    if car in "aeiou":
        print(car)
        count += 1
        
num = [10, 25, 5, 40,15, 30]
nums = int(sum(num))
print(str(nums))
