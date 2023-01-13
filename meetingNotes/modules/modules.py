# James Taddei
# Modules
# 1/10/23

# Brief F-String Rvw
age = 19
name = "John Doe"
print(name + " is " + str(age) + " years old.")
print(f"{name} is {age} years old.")

print()

# Example Custom Module
import exModule
print(exModule.foo())
print(exModule.num2)

print()

# Keywords
from exModule import num1
print(num1)
import math as m
print(m.pi)
print(dir(exModule))

print()

# Time Module
import time
print(time.perf_counter())
time.sleep(2)
print(time.time())

print()

# Math Module
import math
print(math.ceil(0.4))
print(math.fabs(-83))
print(math.factorial(3))
print(math.floor(0.8))
print(math.log(23))
print(math.log10(10_000))
print(math.sqrt(16))
print(math.sin(30))
# Also has cos, tan, asin, acos, atan
print(math.dist([3,2], [4,5]))
print(math.degrees(math.pi))
print(math.radians(180))
print(math.pi)
print(math.e)
print(math.inf)

print()

# Random Module
import random
random.seed(3)
print(random.randint(0, 99))
options = ["a", "b", "c"]
print(random.choice(options))
random.shuffle(options)
print(options)
print(random.random())
