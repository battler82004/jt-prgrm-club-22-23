# James Taddei
# Chained Comparison and Nested Loops
# 10/19/22

# Chained comparison
num = int(input("Enter the pos of the starting letter: "))
num += 64
while (65 <= num < 91): # Checks that num is a letter
    print(f"{num-64}: {chr(num)}")
    num += 1

print()

# Use Cautiously
# Good:
print(0 < 5 <= 6)
print(5 >= 2 > 0)
print(1 == 1 == 1)

print()

# Ok:
a = 3
b = 1
c = 3
print(a != b != c)
print(a != b != c != a)

print()

# Bad:
print(0 < 5 > 3)
print(0 < 7 >= 8 != 7 == 4)

print()

# Nested Loops
for row in range(3):
    currRow = ""
    for column in range(3):
        currRow += f"{row*3+(column+1)} "
    print(currRow)