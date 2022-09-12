# James Taddei
# Basic Commands and Syntax
# 9/11/22

# Basic Arithmetic
x = 5 + 3
print(x)
x = 5 - 3
print(x)
x = 5 * 3
print(x)
x = 5 / 3
print(x)
x = (3 * 7) / 2 # use parenthesis for order
print(x)

print()

# Weird Arithmetic
x = 5 % 3 # modulus operator
print(x)
x = 5 // 3 # floor division
print(x)
x = 5 ** 3 # exponentiation
print(x)

from math import sqrt # square root
x = sqrt(2)
print(x)

print()

# Assignment
x = 5
x += 3 # x = x + 3
print(x)
x -= 2
print(x)
x *= 6
print(x)
x /= 3
print(x)

print()

# Comparison, give boolean result
b = (x == 12)
print(b)
b = (x != 12)
print(b)
b = (x < 15) # <=
print(b)
b = (x > 15) # >=
print(b)

print()

# Combine Comparison
b = ((x == 12) and (False)) # requires both are true
print(b)
b = ((x == 12) or (False)) # requries either is true
print(b)
b = not(True) # ! in most other languages
print(b)

print()

# If/else
if (True):
    print("Is true") # spacing is important in python

if (x == 12):
    print("Is true")

if (x == 15):
    print("Is true") # doesn't print
else:
    print("Is false")
    
if (x == 15):
    print("15")
elif (x == 12):
    print("12")
else:
    print("Other")
    
print()

# Input
# a = input("How many: ")
# print(a)
# in Python 2, raw_input is recommended
