# James Taddei
# Number to Letter Converter
# 9/30/22

# Goal is to output the letter that corresponds to a letter in binary.
# Only for the first 10 letters. 65 = A, 66 = B, etc.

# User input
num = int(input("Enter the number you'd like to convert: "))

# Selecting the corresponding letter
if (num == 65):
    letter = 'A'
elif (num == 66):
    letter = 'B'
elif (num == 67):
    letter = 'C'
elif (num == 68):
    letter = 'D'
elif (num == 69):
    letter = 'E'
elif (num == 70):
    letter = 'F'
elif (num == 71):
    letter = 'G'
elif (num == 72):
    letter = 'H'
elif (num == 73):
    letter = 'I'
elif (num == 74):
    letter = 'J'
else: # If <65 or >74
    print("Error, num is invalid")
    letter = "ERROR"

# Output
print(f"The letter that corresponds to {num} is " + letter)