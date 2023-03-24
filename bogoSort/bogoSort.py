# James Taddei
# Bogo Sort Implementation
# 3/24/23

from random import shuffle

def main():
    lst = [64, 25, 12, 22, 11]
    print(f"Sorted list: {bogoSort(lst)}")

def bogoSort(lst: list) -> list:
    """
    Returns a sorted version of the inputted list (via bogo sort).
    """
    isSorted = False
    while not(isSorted):
        shuffle(lst)

        # Check if list is sorted
        isSorted = True
        for i in range(len(lst)-1):
            if (lst[i] > lst[i+1]):
                isSorted = False
                break # List is unsorted
    
    return lst

main()