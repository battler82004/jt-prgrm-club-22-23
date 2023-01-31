# James Taddei
# Files
# 1/23/23

# Basic Example
f1 = open("/Users/james.taddei/Desktop/Programming Club 22-23/Meeting 12 Stuffs/files/file.txt")
data1 = f1.read()
f1.close()
print(data1)

print()

# Readlines
fileName2 = "/Users/james.taddei/Desktop/Programming Club 22-23/Meeting 12 Stuffs/files/demoFolder/demoFolder.txt"
with open(fileName2) as f2:
    data2 = f2.readlines()
    print(data2)

print()

# Readline
with open(fileName2) as f2:
    data3 = f2.readline()
    print(data3)

print()

# Seek
with open(fileName2) as f2:
    f2.seek(10)
    data3 = f2.readline()
    print(data3)

print()

# Write
fileName3 = "/Users/james.taddei/Desktop/Programming Club 22-23/Meeting 12 Stuffs/files/demoFolder/ex.txt"
with open(fileName3, "w") as f3: # write
    f3.write("Hello ")
with open(fileName3, "a") as f3: # append writing
    f3.write("World!")
with open(fileName3) as f3: # output
    print(f3.read())