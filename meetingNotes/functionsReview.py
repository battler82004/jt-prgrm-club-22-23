# James Taddei
# Functions Review
# 11/3/22

# Quadratic Func Example
# f(x) = x^2 + 3x + 7
def f(x):
    print(x ** 2 + 3 * x + 7)
f(3)
f(6)

print()

# Return
def f(x):
    return x ** 2 + 3 * x + 7
y = f(3)
print(f"f(3) = {y}")

print()

# Type Hinting
def f(x: float) -> float:
    return x ** 2 + 3 * x + 7
y = f(3)
print(f"f(3) = {y}")
print(f"f(7) = {f(7)}")

print()

# 2 Parameters
def f(x: float, y: float) -> float:
    return x ** 2 + y ** 2
y = f(3,6)
print(f"f(3,6) = {y}")
print(f"f(7,4) = {f(7,4)}")
# print(f"f(7) = {f(7)}") # causes error

print()

# Default Values
def f(x: float, y: float = 0) -> float:
    return x ** 2 + y ** 2 - 9  
y = f(3,5)
print(f"f(3,5) = {y}")
print(f"f(7) = {f(7)}")

print()

# Beyond Just Print/Return
def f(x: float, y: float = 0) -> float:
    x += 1
    y -= 1
    return x ** 2 + y ** 2 - 9
y = f(3,5)
print(f"f(3,5) = {y}")
print(f"f(7) = {f(7)}")

print()

# Is In
def main():
    print(f"+ = {isIn('+')}")
    print(f"p = {isIn('p')}")
def isIn(x):
    operations = "+-*/"
    if (x in operations):
        return True
    else:
        return False
main()

print()

# Is Not In
def main():
    print(f"+ = {isNotIn('+')}")
    print(f"p = {isNotIn('p')}")
def isNotIn(x):
    operations = "+-*/"
    return x not in operations
main()