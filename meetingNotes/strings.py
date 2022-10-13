# James Taddei
# Strings
# 10/8/22

string = "hello world!"
#         0123456789
#				   -3

# Indexing
char = string[4]
print(char)
char = string[10]
print(char)
char = string[-3] # reverse indexing, starts at -1
print(char)

print()

# Indexing a Range
s = string[0:5] # 0 <= char < 5
print(s)
s = string[:5]
print(s)
s = string[3:]
print(s)

print()

# Reverse a String
s = string[::-1]
print(s)

print()

# Length of String
print(len(string))

print()

# String Methods
n = string.count("l")
print(n)
i = string.find("o") # returns -1 if not found
print(i)
i = string.index("ld") # throws an error if not found
print(i)
i = string.upper()
print(i)
print(string)
i = i.lower()
print(i)
s = "  ajdsf  "
s = s.strip()
print(s)
num = "7"
num = num.zfill(3)
print(num)

print()

# Escape Characters
print("Hello\tworld")
print("Hello\\world")
# print("Hello"world") # causes an error
print("Hello\"world")
print("Hello'world")
print('Hello\'world')
print("'Hello\nworld\n!'")

print()

# F-strings
f = """'Hello
world
!'"""
print(f)
num = 7
f = f"Hello {num} world"
print(f)