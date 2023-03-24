# James Taddei
# Stalin Sort Implementation
# 3/24/23

def main():
    lst = [22, 11, 84, 33, 64, 25, 12, 22, 11, 87, 12]
    print(f"Sorted list: {stalinSort(lst)}")

def stalinSort(lst: list) -> list:
    """
    Returns a sorted version of the inputted list (via stalin sort).
    """
    i = 0
    while (i < (len(lst)-1)):
        if (lst[i+1] < lst[i]):
            lst.pop(i+1)
        else:
            i += 1

    return lst

main()