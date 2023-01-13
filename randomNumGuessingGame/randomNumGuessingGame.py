# James Taddei
# Random Num Guessing Game
# 1/13/23

from random import randint

def main():
    # Variable declaration
    answer = randint(1,100)
    numOfGuesses = 0

    while (True):
        # Increment the counter and prompt for a new guess
        numOfGuesses += 1
        guess = int(input("Enter a guess: "))

        # Determine output based on guess
        if (guess == answer):
            print(f"You found the number, {answer}, in {numOfGuesses} guesses!")
            break
        elif (guess > answer):
            print(f"Your guess is too high.")
        else:
            print(f"Your guess is too low.")

main()