# James Taddei
# Functions
# 10/19/22

# Basic Function
def func(x):
    print(x)
    print(x-1)
    print()

func(7)
func(12)

print()

# Solve a problem
def pow(base, exponent):
    curr = 1
    for _ in range(exponent):
        curr *= base
    print(curr)

pow(2,3)
pow(10,4)

print()

# Method
print("7".zfill(3))

print()

# Default Values
def isTrue(val=0):
    if (val):
        print("Yes")
    else:
        print("No")

isTrue(7)
isTrue()

print()

# Keyword Arguments (Setting Specific Vals)
def myFunc(needs, foo=7, bar=9):
    print(needs)
    print(foo)
    print(bar)
    print()

myFunc(2)
myFunc(5, 6)
myFunc(5, bar=6)
myFunc(5, bar=3, foo=4)

print()

# Value Returning
def pow(base, exponent): # Don't redefine in actual code
    curr = 1
    for _ in range(exponent):
        curr *= base
    return curr

pow(2,3)
print(pow(10,4))

print()

# Data Types
def plus(x: float, y: float) -> float:
    return x + y

print(plus(2.5,3.2))
print(plus("hello","world"))

print()

# Pass Function and Single Return
def passFunc():
    pass
def seven(x):
    return 7

passFunc()
print(seven())

print()

# Scope World Example
globalPop = 8_000

def canada():
    canadaPop = 40
    print(f"Canada Pop: {canadaPop}")
    print(f"Global Pop: {globalPop}")

def america():
    pop = 330
    print(f"America Pop: {pop}")
    # print(f"Canada Pop: {canadaPop}") # causes an error

def mexico():
    pop = 130 # can reuse names, arguable if should
    print(f"Mexico Pop: {pop}")
    
canada()
america()
mexico()

print()

# Main Function
def main():
    num = float(input("Num: "))
    print(plusSeven(num))

def plusSeven(num: float) -> float:
    return num + 7

main()