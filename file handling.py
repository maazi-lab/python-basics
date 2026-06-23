# open file
file = open("student.txt", "w")
file.write("Echezona")
file.close()

#shortcut to open file
with open("student.txt", "w") as file:
    file.write("Echezona")

# read and deplay text
file = open("student.txt","r")
content = file.read()
print(content)

# add in file (append):
with open("student.txt", "a") as file:
    file.write("\nFavour Miracle")
    print("name saved!!")
    
# read and display!!
with open("student.txt", "r") as file:
    content = file.read()
    print(content)
    
# save three names
with open("student.txt", "w") as file:
    file.write("Goodness\n")
    file.write("Mary\n")
    file.write("Favour\n")
print("student saved")

# read all name from student.txt
with open("student.txt", "r") as file:
    content = file.read()
    print(content)

# ask for name and saved in file
name = input("enter you name:")
with open("student.txt", "a") as file:
    file.write(name + "\n")
    print("name saved")
    
# ask for five names
with open("student.txt", "a") as file:
    for i in range(5):
        name = input("enter name" + str(i + 1) + ": ")
        file.write(name + "\n")
print("Name saved!!")

# read file line by line!!
with open("student.txt", "r") as file:
    for  line in file:
        print(line.strip())
        
# create note in diary
note = input("write your note:")
with open("diary.txt", "r") as file:
    file.write(note)
print(" note save")

# read it back
with open("diary.txt", "r") as file:
    file.read()