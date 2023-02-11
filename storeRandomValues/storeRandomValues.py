# James Taddei
# Store Random Values
# 1/26/23

import random

def main():
    fileLoc = "/Users/james.taddei/Desktop/Programming Club 22-23/"
    fileLoc += "Meeting 12 Stuffs/storeRandomValues/text.txt"

    with open(fileLoc, "w") as file:
        for _ in range(10):
            file.write(str(randomRGB()) + "\n")
        for _ in range(10):
            file.write(randomString() + "\n")
        for _ in range(10):
            file.write(str(randomMultipleOf7()) + "\n")

def randomRGB() -> list:
    """
    Returns a list holding 3 random integers which acts
    as an RGB value.
    """
    rgbValue = []
    for _ in range(3):
        rgbValue.append(random.randint(0, 255))

    return rgbValue

def randomString() -> str:
    """
    Returns a 10 character long string holding random
    letters.
    """
    string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(10):
        string += random.choice(alphabet)

    return string

def randomMultipleOf7() -> int:
    """
    Returns a random multiple of 7 between 0 and
    70 (inclusive).
    """
    return (7 * random.randint(0, 10))

main()