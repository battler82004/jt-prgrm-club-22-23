# James Taddei
# Input Errors
# 5/1/23

def main():
    print(f"Number of players: {numberOfPlayers()}")

def numberOfPlayers() -> int:
    """
    Returns the number of players entered by the user. If
    there is a problem, the program will prompt the user to
    reenter.
    """
    while (True): # Runs until valid input
        try:
            num = int(input("Enter the number of players: "))
        except: # NaN inputted
            print("Error, entered value is not a number. Try again.")
        else:
            if ((num == 1) or (num == 2)): # Num is valid
                return num
            # Invalid num
            print("Error, the entered number is not 1 or 2. Try again.")

main()