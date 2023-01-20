# James Taddei
# Binary Search Implementation
# 1/19/23

def main():
    lst = [2, 3, 4, 10, 40]
    target = 10
    pos = binarySearch(lst, target)
    if (pos == -1):
        print(f"{target} is not in the list.")
    else:
        print(f"{target} is at index {pos}.")

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

main()