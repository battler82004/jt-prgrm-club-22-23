# James Taddei
# Exceptions
# 5/1/23

# Raises a div by 0 error if divisor is 0
# x = 0
# if (x == 0):
#     raise ZeroDivisionError("Cannot divide by zero")
# else:
#     print(5 / x)

print()

# Try
try:
    print("1")
    raise ZeroDivisionError("Error")
    print("Also error")
except:
    pass
print("2")

print()

# Except, won't run
try:
    print(5 / 1)
except:
    print("There was an error")

print()

# Except, will run
try:
    print(5 / 0)
except:
    print("There was an error")
    print(float("Inf"))

print()

# Different Exceptions for Types
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Div by 0")
except NameError:
    print("Name error")
except:
    print("Other error")

print()

# Else and Finally
num = 5
try:
    x = 1 / num
except:
    print("Infinite result") # imagine this is a log
else:
    print("Finite result") # imagine this is a log
finally:
    print("Calculation complete")