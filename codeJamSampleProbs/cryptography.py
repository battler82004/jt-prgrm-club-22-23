# James Taddei
# Cryptography (Code Jame Sample Probs #2)
# 12/9/22

"""
Prompt:
Cryptography is about protecting information. Early schemes involved switching letters. A common
approach was using an encoding wheel that "moved" every letter the same number of letters down in
the alphabet. The letters on the wheel "wrap around" (a follows z). Write a program that accepts an
integer n and a word less than 10 letters long. Print out the encoded word with every letter replaced
by the nth successor.
"""

def main():
    letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    shiftNum, text = (input("input: ")).split()
    shiftNum = int(shiftNum)

    encrypted = ""

    # Go through each letter and change it out for the encrypted version
    for i in range(len(text)):
        if (text[i] == text[i].lower()): # Lowercase
            # Find where the new letter is and add it
            newLetterIndex = letters.index(text[i]) + shiftNum
            encrypted += letters[newLetterIndex]
        else: # Uppercase
            letter = text[i].lower()
            newLetterIndex = letters.index(letter) + shiftNum
            encrypted += letters[newLetterIndex].upper()

    print(f"output: {encrypted}")

main()