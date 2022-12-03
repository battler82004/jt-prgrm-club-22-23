# James Taddei
# Swap Values
# 11/11/22

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    swapValues(numbers, 3, 5)
    print(numbers)

def swapValues(lst: list, num1: int, num2: int) -> None:
    """
    Swaps the indexes of the first instances of the two inputted
    numbers.
    """
    if (num1 == num2): # Can't swap same value
        return
    if (num1 not in lst):
        print(f"Error, value 1 ({num1}) is not in the list")
        return
    if (num2 not in lst):
        print(f"Error, value 2 ({num2}) is not in the list")
        return
    # Find and swap instances
    pos1 = lst.index(num1)
    pos2 = lst.index(num2)
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

main()