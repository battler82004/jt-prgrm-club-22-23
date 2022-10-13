# James Taddei
# Number to Letter Converter
# 10/12/22

# Variable declaration
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# User input
num = int(input("Enter num: "))
num -= 65

# Final output
if (num < 0):
    print("Num too small")
elif (num > 25):
    print("Num too big")
else: # Valid number
    print(alphabet[num])
