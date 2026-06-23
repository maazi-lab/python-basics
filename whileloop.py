i = 0 
while i <= 5:
    print(i)
    i += 1
    
# print odd numbers
i = 1
while i <= 20:
    print(i)
    i += 2
# count down
i = 10
while i >= 0:
    print(i)
    i -= 1
# multiplication in while loop
count = 1
while count <= 10:
    print("4 x ", count, "=", 4 * count)
    count += 1
# keep asking until get the number
num = ""
while num != 99:
    num = int(input("enter your number:"))
    print("Game over")
# adding of number
num = 1
while num <= 50:
    print(num + num)
    num += 1
# find reminder and continue counting
num = 1
while num <= 20:
    if num % 3 == 0:
        print(num)
        num += 1
        continue
number = num + 1
print(number)

# asking of number using input and while loop
scret = ""
while scret != 3456:
    scret = int(input("enter your scret:"))
    print("correct")

# count down
count = 20
while count >= 1:
    print(count)
    count -= 2

# using while true in while loop
total = 0
while True:
    number = int(input("enter yuor number(0 to stop):"))
    if number == 0:
        print("stop")
        break
    
    total = total + number
    print(str(total))
    
print("final: " + str(total))

i = 1
while i <= 5:
    print((str(i) + " ") * i)
    i = i + 1



