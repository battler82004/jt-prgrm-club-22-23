# James Taddei
# Bubble Sort Implementation
# 3/22/23

# Possible implementations for outer loop: check for swaps,
# for loop, check is sorted

def main():
    lst1 = [5, 1, 4, 2, 8]
    print(f"Sorted list (while): {bubbleSort(lst1)}")

    lst2 = [5, 1, 4, 2, 8]
    print(f"Sorted list (for): {bubbleSortWithFor(lst2)}")

    lst3 = [5, 1, 4, 2, 8]
    print(f"Sorted list (check): {bubbleSortWithCheck(lst3)}")

def bubbleSort(lst: list) -> list:
    """
    Returns a sorted version of the inputted list (via bubble sort).
    """
    length = len(lst) - 1 # skip last element
    hasChanged = True
    # Checks that a change has occured meaning that the list may not be fully sorted
    while (hasChanged):
        hasChanged = False
        for i in range(length): # Goes through each element to find if a swap is needed
            if (lst[i] > lst[i+1]):
                hasChanged = True
                lst[i], lst[i+1] = lst[i+1], lst[i] # actual swap
    
    return lst

def bubbleSortWithFor(lst: list) -> list:
    """
    Returns a sorted version of the inputted list (via bubble sort).
    A for loop is used to determine when the sorting is done.
    """
    length = len(lst)
    for i in range(length): # Thru each element
        for j in range(length-i-1): # Last i elements are in place
            if (lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

def bubbleSortWithCheck(lst: list) -> list:
    """
    Returns a sorted version of the inputted list (via bubble sort).
    Checks on each loop through the list if it is sorted.
    """
    length = len(lst) - 1 # skip last element
    isSorted = False
    # Keep looping until the list is sorted
    while not(isSorted):
        for i in range(length): # Goes through each element to find if a swap is needed
            if (lst[i] > lst[i+1]):
                lst[i], lst[i+1] = lst[i+1], lst[i] # swap

        isSorted = True
        for i in range(length):
            if (lst[i] > lst[i+1]):
                isSorted = False
                break # List is unsorted

    return lst

main()