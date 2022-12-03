# James Taddei
# Square Items
# 11/11/22

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    squareItems(numbers)
    print(numbers)

def squareItems(lst: int) -> None:
    """
    Squares all of the values in an integer list.
    """
    for i in range(len(lst)):
        val = lst[i]
        lst[i] = val * val

main()