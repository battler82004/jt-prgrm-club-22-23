# James Taddei
# Uppercase Function
# 10/19/22

def uppercase(lowercase: str) -> str:
    """
    This function turns an inputted string into the uppercase version of itself
    which is then returned.
    """
    newString = ""
    for char in lowercase:
        num = ord(char) - 32 # Letter -> binary num, shifted 32 to be upper
        if ((num < 65) or (num > 91)): # not a lowercase letter, just copy
            newString += char
            continue
        newString += chr(num) # Is lowercase letter

    return newString

print(uppercase("Hello World!"))