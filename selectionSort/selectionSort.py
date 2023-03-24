# James Taddei
# Selection Sort Implementation
# 3/22/23

def main():
    lst = [64, 25, 12, 22, 11]
    print(f"Sorted list: {selectionSort(lst)}")

def selectionSort(lst: list) -> list:
    """
    Returns a sorted version of the inputted list (via selection sort).
    """
    length = len(lst) # skip last element

    # As many moves as there are elements in the list (-1)
    for i in range(length):
        minPos = i
        for j in range(i + 1, length): # Finds the new min value index
            # Can use i+1 because minPos is 'i' by default
            if (lst[j] < lst[minPos]):
                minPos = j
        lst[i], lst[minPos] = lst[minPos], lst[i]

    return lst

main()