# James Taddei
# My Uppercase
# 10/12/22

# Variable declaration
string = "HelloWorld"
newString = ""

for letter in string:
    if (letter.isupper()): # If already upper, just copy letter
        newString += letter
        continue
    
    # Is lowercase
    num = ord(letter) - 32
    newString += chr(num)

# Final output
print(newString)