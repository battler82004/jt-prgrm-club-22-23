# James Taddei
# Longest 7-Segment Word
# 1/26/23

def main():
    # Variable declaration
    longestWord = ""
    longestLen = 0
    fileLoc = "/Users/james.taddei/Desktop/Programming Club 22-23/"
    fileLoc += "Meeting 12 Stuffs/longest7SegWord/englishWords.txt"

    # Look at each word in the file and determine if it is longer
    # than the current longest and has no invalid letters
    with open(fileLoc) as dictionary:
        for word in dictionary:
            length = len(word)
            if (length > longestLen) and (isValidWord(word)):
                longestLen = length
                longestWord = word
    
    print(f"The longest word is {longestWord} at {longestLen} letters.")
    # Should get: dichlorodiphenyltrichloroethane at 31 letters

def isValidWord(word: str) -> bool:
    """
    Returns if the inputted word includes an invalied letter (one
    which cannot be displayed by a 7-segment screen).
    """
    word = word.lower()
    invalidLetters = "gkmqvwxz"

    for letter in invalidLetters:
        if (letter in word):
            return False

    return True

main()