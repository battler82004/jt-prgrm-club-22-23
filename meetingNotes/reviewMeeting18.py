# James Taddei
# Review Meeting 18
# 5/12/23

if (True): # Meeting 15 (Bubble and Selection Sort)
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
    
    lst1 = [5, 1, 4, 2, 8]
    print(f"Sorted list: {bubbleSort(lst1)}")
    print(f"List: {lst1}")

    print()

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

    lst2 = [64, 25, 12, 22, 11]
    print(f"Sorted list: {selectionSort(lst2)}")

print("\n")

if (True): # Meeting 16 (Big O Notation)
    # O(1)
    n = 1
    print(n)

    print()

    # O(log n)
    def binarySearch(lst: list, target: int) -> int:
        """
        Returns the index of the target if present, otherwise
        returns -1.
        """
        low = 0
        high = len(lst) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            if lst[mid] < target: # ignore left
                low = mid + 1
            elif lst[mid] > target: # ignore right
                high = mid - 1
            else: # found target
                return mid

        return -1 # target not in list
    print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 8))

    print()

    # O(n)
    n = 5
    for i in range(n):
        print(i)

    print()

    # O(n^2)
    n = 5
    for i in range(n):
        for j in range(n):
            print(i*n+j)

print("\n")

if (True): # Meeting 17 (Exceptions)
    # "Natural" Error
    # print(5 / 0)

    print()

    # Raise
    # raise Exception("Error message.")

    print()

    # Try Except, won't run
    try:
        print(5 / 1)
    except:
        print("There was an error")

    print()

    # Try Except, will run
    try:
        print(5 / 0)
    except:
        print("There was an error")
        print(float("Inf"))

    print()

    # Different Exceptions for Types
    try:
        print(x)
    except ZeroDivisionError:
        print("Div by 0")
    except NameError:
        print("Name error")
    except:
        print("Other error")

    print()

    # Else and Finally
    num = 5
    try:
        x = 1 / num
    except:
        print("Infinite result") # imagine this is a log
    else:
        print("Finite result") # imagine this is a log
    finally:
        print("Calculation complete")