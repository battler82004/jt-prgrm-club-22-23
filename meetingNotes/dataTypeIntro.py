# James Taddei
# Data Types Intro
# 9/11/22

# Ints, floats, bools, chars, strings

# Integer (int)
i = 5
print(i)
i = int(7_200_000)
print(i)

# In C++, "int x = 5;"
# Can't change type in most languages
print()

# Float / double, named due to floating deci point
f = 5.5
print(f)
f = float(2_110.100) # Double is not command in Python
print(f)

print()

# Boolean (bool)
b = True
print(b)
b = bool(0)
print(b)

print()

# Char
c = 'Q'
print(c)
c = "/"
print(c)

print()

# String (str)
s = "hello world!"
print(s)
s = str(5)
print(s)

print()

# Types don't mix well
x = int(5) + float(5.5)
print(x)
i = "asdf"
print(i)

print()

# print(5 + "5.5")
print(5 + float("5.5"))
print(5, "5.5")
print(str(5) + "5.5")
print(f"{5}5.5") # only works in Python 2
print("{}5.5".format(5))

#Understanding basic data type converters
#type() outputs the type of the object you provide. example shown below.
message = "This is a string :)"
number = 12345
print(type(message))
print(type(number))

#str() converts data type to a string. example shown below.
age = 31
print("Python is " + str(age) + " years old!")

#int() converts data type to an integer. example shown below.
currentAge = input("Enter your current age ") #input function always returns string
futureAge = int(currentAge) + 10 
print("You will be " + str(futureAge) + " years old in 10 years")

#float() converts data type to a float. example shown below.
money = float(input("How much money do you have"))
pencilCost = 0.50
folderCost = 1.89
notebookCost = 2.56
totalCost = money - pencilCost - folderCost - notebookCost
print("Your total after buying supplies is " + str(totalCost) + " dollars")
