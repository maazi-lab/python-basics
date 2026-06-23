def greet(name):
    print("=" * 30)
    print("Hello:" + name + "!")
    print("Welcome To Python")
    print("=" * 30)
    
greet("Echezona")
greet("Miracle")
greet("John")


def human(name, age):
    print("My name: " + name + "!")
    print("My age: " + str(age) + " years old")
    print("=" * 30)

human("Echezona", 20)
human("Emeka", 25)
human("Sunday", 45)
human("John", 34)

def number(a, b):
    result = a + b
    return result

answer = number(10, 45)
print("answer:" + str(answer))


def one(d, g):
    result = d + g
    return result

answer = one(45, 79)
print("ANSWER: " + str(answer))

def goods(price, quantity):
    bills = price * quantity
    return bills

total = goods(450, 3500)
print("total: " + str(total))

def moni(num, num2, num3):
    total = num + num2 * num3
    return total

mon = moni(45, 49, 50)
print("total mon: " + str(mon))

def kate(name = "john"):
    print("Hello " + name + "!")
    
kate("name")
kate()    

def john(name = "favour"):
    print("My name is " + name + "!")
    
john("myrak")
john()

def electricity_bill(unit):
    per_unit_price = 85
    total = unit * per_unit_price
    vat = total * 0.0075
    final = total + vat
    return final

bill = electricity_bill(300)
bill1 = electricity_bill(450)
bill2 = electricity_bill(350)

print("300 unit: N "+ str(bill))
print("450 unit: N " + str(bill1))
print("bill2 unit: N " + str(bill2))

def score_grade(score):
    if score >= 85:
        return "A = Excellent!"
    elif score >= 70:
        return "B = Very Good!"
    elif score >= 60:
        return "C = Good!"
    elif score >= 50:
        return "D = Pass!"
    else:
        return "F = Failed"
    
stud1 = score_grade(84)
stud2 = score_grade(67)
stud3 = score_grade(56)

print("Score: " + str(stud1))
print("Score: " + str(stud2))
print("Score: " + str(stud3))


def item(earning, spending):
    income = earning - spending
    if income >= 100000:
        return "Rich Man!"
    elif income >= 80000:
        return "Big Man!"
    elif income >= 50000:
        return "Middile Man!"
    else:
        return "Poor Man!"
    
level = item(450000, 330000)
level1 = item(550000, 474000)
level2 = item(670000, 568000)

print("Acct: N " + str(level))
print("Acct: N " + str(level1))
print("Acct: N " + str(level2))    

def grace():
    print("Hello")


grace()

def welcome():
    print("Welcome To Class:")
    
welcome()

def names(name):
    print("Hello", name)
    
names("Mary")
names("Miracle")

def add():
    print(5 + 3)
    
add()

def add():
    print(4 * 6)
    
add()

def men():
    print(28 - 16)
    
men()

def man():
    print(45 / 5)
    
man()

def meni(a, b):
    result = (a + b)
    return result
    
age = meni(30, 45)
print("Big age: " + str(age))

def greet():
    print("HELLO")
    
greet()

def welcome():
    print("Welcome to python class")
    
welcome()
def function():
    print("Unique Secondary School")
    
function()
def country():
    print("Nigeria")
    
country()

def  food():
    print("Your favourite food")
    
food()
def sport():
    print("Your sport")
    
sport()

def tech():
    print("technology is fun")
    
tech()

def motivated():
    print("keep learning")
    
motivated()

def show(age):
    print("You are", age, 'years old')
    
show(15)
show(67)
show(45)

def mazi():
    name = input("Enter yuor name:")
    print("Hello", name)
    
mazi()
    
def welcome():
    me = input("Enter your name:")
    print("Welcome", me)
    
welcome()
welcome()
welcome()

def greet():
    print("welcome to myraktech")
    
    
    