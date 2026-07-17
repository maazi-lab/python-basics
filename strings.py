# File: strings.py
# Demonstrates string manipulation methods and formatting.

name = "maazi miracle"
print(name.upper())
print(name.title())
print(name.lower())
print(name.replace("maazi", "chief"))
print(name.count("a"))
print(name.find("m"))
print(name.startswith("ma"))
print(name.endswith("le"))

# split words
names = "maazi miracle"
print(name.split())

# join items
fruit = ["apple", "mango", "orange"]
print("-".join(fruit))

# removing of space
name = "   john   "
print(name.strip())

# capitalize
name = "hello world"
print(name.capitalize())


name = input("enter your name: ")
print(name.upper())
sent = input("enter sentence: ")
print(sent.lower())
print(sent.replace("cat", "dog"))
word = "appear"
print(word.count("a"))
print(word.startswith("py"))

name = "echezona"
city = "lagos"
mesaaage = "learning python"
print(name[0])
print(name[1])
print(name[2])
print(name[4])  
name = "Myraktech"
print(name[1:3])
print(name[3:7])
print(name[4:9])
print(name[2:8])
print(name[-1])
print(name[-2])
print(name[:5])
print(name[5:])
print(name[::-1])
name = "miracleTech"
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.lower())

name2 = "miraclezona"
print(name2.strip())
print(name2.lstrip())
print(name2.rstrip()) 

sentence  = "I love python"
print(sentence.replace("python", "AI"))
print(sentence.split(" "))
print(len(sentence))
print(sentence.count("0"))
print(sentence.find("love"))
print(sentence.upper())


name = "myraktech"
age = 20
course = "Artificial Intelligent"
print(f"My name is {name} and i am {age} years old")
print(f"I study {course}")
print(f"in 5 years old i wil be{age + 5}years old")

sent = "I love python and ai"
print("python" in sent)
print("ai" in sent)
print("java" in sent)
print("java" not in sent)

num = "Technology"
print(num.upper())

dream = "I am learnig AI"
print(dream.replace("AI", "python"))
nig = "I live in lagos Nigeria"
print(f"Nigeria" in nig)

learn = "Artificial Intelligent"
print(learn[::-1])
print(len(learn))

# hard
name = "Echezona"
print(name.upper)
sentence = "I am learning python and ai"
print(sentence[:10])
user = input("enter your name:")
print(f"Welcome {name} to Myraktech")
city = "Lagos state"
print(city[::-1])
length = "Artificial intelligent"
print(length.count("a"))

sent = input("enter youe sentence")
print(len(sent))
# harder
user = input("enter your word")
print(user.rstrip())
print(user.strip())
print(user.lstrip())

sent1 = ("Python is the best programing language")
print(sent1.replace("best", "greatest"))

name1 = input("enter your name:")
print(name.split("Onweh"))

sent2 = "I am from Lagos Nigeria"
print("Nigeria" in sent2)

sentence = "i am a nigerian"
print(sentence.title())

string = " myraktech"
print(string.strip())
print(string.rstrip())
# hardest

password = "myrak123"
if "myrak" in password:
    print("strong password")
else:
    ("weak password")
    
sentence = input("enter your sentence:")
print(len(sentence))

age = input("enter your age:")
name = input("enter your name:")
print(f"in 10 yeras {name} will be {str(age + 10)} yerars old")

character = "Characters"
print(character[:5])
print(character[5:])
print(character[:5:])

word = input("enter your word:")
print(word.startswith("A"))
print(word.endswith("e"))

# replace with vowel with **
sentence = input("Type your sentence:")
print(sentence.replace("a", "*"))
print(sentence.replace("e", "*"))
print(sentence.replace("i", "*"))
print(sentence.replace("o", "*"))
print(sentence.replace("u", "*"))
