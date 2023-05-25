# James Taddei
# Overlap (HSPC 2019 #10)
# 5/24/23

"""
Extra examples:
Blocking- 2, 9, 7, 5, 1, 6; should block 4
Multiple blocks- 9, 2, 4, 6, 3, 8; should block 1, 5, or 7
Multiple wins- 2, 5, 6, 4, 8, 3; should win 1 or 7
"""

def main():
    """
    Prompts the user to input 6 tic tace toe moves into a
    magic square and outputs if either has side has won.
    If neither has, any winnning moves will be outputted.
    If there aren't any winnig moves, moves which block the
    opponent from winning will be outtputed.
    """
    # Variable declaration
    board = [""]*10 # 0th pos is unused
    xSquares = []
    oSquares = []

    enterMoves(board) # user input

    # Determines if X or O has already won
    for num, pos in enumerate(board):
        if (pos == 'X'):
            xSquares.append(num)
        elif (pos == 'O'):
            oSquares.append(num)

    if (sum(xSquares) == 15):
        print("X has already won")
        return
    if (sum(oSquares) == 15):
        print("O has already won")
        return

    # Outputs any of X's winning moves
    needed = findWinningSquares(xSquares, oSquares)
    if (len(needed) == 3):
        print(f"Play {needed[0]}, {needed[1]}, or {needed[2]} to win")
        return
    if (len(needed) == 2):
        print(f"Play {needed[0]} or {needed[1]} to win")
        return
    if (len(needed) == 1):
        print(f"Play {needed[0]} to win")
        return

    # Outputs any of X's blocking moves
    needed = findWinningSquares(oSquares, xSquares)
    if (len(needed) == 3):
        print(f"Play {needed[0]}, {needed[1]}, or {needed[2]} to block")
        return
    if (len(needed) == 2):
        print(f"Play {needed[0]} or {needed[1]} to block")
        return
    if (len(needed) == 1):
        print(f"Play {needed[0]} to block")
        return

    print("Neither side has won, and X has no winning or blocking moves.")

def enterMoves(board: list) -> None:
    """
    Prompts the user to input 6 tic tace toe moves into the
    inputted magic square list.
    """
    moves = ["first X", "first O", "second X", "second O", "third X", "third O"]
    for move in moves:
        pos = int(input(f"Enter {move} move: "))
        board[pos] = move[-1]

def findWinningSquares(squares1: list, squares2: list) -> list:
    """
    Determines which (leagal) squares would allow the player
    from the first inputted list to win. Squares which are
    already taken are illegal moves and thus filtered out.
    """
    # Variable declaration
    needed = []
    legalNeeded = []
    combs = ((squares1[0] + squares1[1]), (squares1[1] + squares1[2]), (squares1[0] + squares1[2]))

    # Determines which squares are needed to win and stores them in 'needed'
    for comb in combs:
        currNeeded = 15 - comb # 2 existing plus new need to total 15
        # checks that the needed square actually exists
        if ((1 <= currNeeded) and (currNeeded <= 9)):
            needed.append(currNeeded)

    for pos in needed: # filters illegal moves (already taken squares)
        if ((pos not in squares1) and (pos not in squares2)):
            legalNeeded.append(pos)

    return legalNeeded

main()