# Team #9 (James Taddei, Jonathan Duffy, Ethan Ruch, Jayden Lawrence)
# Question 1 (ACM Code Jam, DeSales University)
# 12/20/22

"""
Description: This program takes in 4 2-letter words and finds the combination of two words that
when in a 2 by 2 grid ("crossword") forms all four of the words.
Ex:
    Input: ab ab aa bb
    Ans: ab ab
    a b
    a b
    Left side: aa, right side: bb, top: ab, bot: ab
Ex:
    Input: ab ab ab aa
    Ans: none (can't make 3 ab's)
"""

def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    word3 = input("Enter the third word: ")
    word4 = input("Enter the fourth word: ")
    words = [word1, word2, word3, word4]
    words.sort()

    combs = [[word1, word2], [word1, word3], [word1, word4], [word2, word3], [word2, word4], [word3, word4]]

    for comb in combs:
        one = comb[0]
        two = comb[1]
        newWords = [one, two, one[0] + two[0], one[1] + two[1]]
        newWords.sort()
        if (words == newWords):
            print(one + "\n" + two)
            return

    print("No solution")

main()
