# James Taddei
# Loops
# 10/8/22

# While Loop
string = "34"
while (len(string) < 7):
    string = "0" + string
print(string)
print("1234567")

print()

# Accidentally Infinite Loop
# while (string != "123"):
#     print(string)

# Intentionally Infinite Loop
# while (True):
#     print(string)

# Couting While Loop
i = 0
while (i < 7):
    print(i)
    i += 1

print()

# Else
i = 0
while (i < 7):
    print(i)
    # if (i == 3): # won't happen if breaks
    #     break
    i += 1
else:
    print("didn't break")
    
print()
    
# Do While V1
i = 3
b = True
while (b):
    print(i)
    i += 1
    b = (i == 7)
    
print()

# Do While V2
i = 3
isFirst = True
while (isFirst or (i == 7)):
    isFirst = False
    print(i)
    i += 1
    
print()

# For Loop
for i in range(7):
    print(i)
    
print()

# Plus 2
for i in range(0,7,2):
    print(i)
    
print()

# Loop Through String
string = "hello"
for char in string:
    print(char)
    
print()

# Loop Through String w/ Indexing
for i in range(len(string)):
    print(string[i])
    
print()
    
# Else
for i in range(len(string)):
    print(string[i])
    # if (string[i] == "l"):
    #     break
else:
    print("didn't break, l not found")
    
print()

# Break
for i in range(7):
    if (i == 3):
        break
    print(i)
    
print()

# Continue
for i in range(7):
    if (i == 3):
        continue
    print(i)