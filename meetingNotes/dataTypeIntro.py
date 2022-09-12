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
