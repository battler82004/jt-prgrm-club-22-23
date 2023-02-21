# James Taddei
# Word Frequency
# 1/26/23

def main():
    # Variable declaration
    fileLoc = "/Users/james.taddei/Desktop/Programming Club 22-23/"
    fileLoc += "Meeting 12 Stuffs/wordFrequency/text.txt"
    words = []

    # Get a list of all of the words in the file
    with open(fileLoc) as file:
        for line in file:
            words.extend(line.split())

    # Make all of the words all lowercase
    for i in range(len(words)):
        words[i] = words[i].lower()
    
    # Sort the list of words before going through each
    # word and outputting its number of occurances if
    # it hasn't yet been outputted
    words.sort()
    last = ""
    for word in words:
        if (word == last):
            continue
        last = word
        print(f"{word}: {words.count(word)}")

main()