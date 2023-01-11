# Team #9 (James Taddei, Jonathan Duffy, Ethan Ruch, Jayden Lawrence)
# Question 4 (ACM Code Jam, DeSales University)
# 12/20/22

"""
Description: This program takes in a sentence on the first line and outputs the words sorted
alphebetically line-by-line (with capital letters coming before all lowercase letters).
"""

sentence = (input("Enter the sentence: ")).split()
sentence.sort()

for word in sentence:
    print(word)