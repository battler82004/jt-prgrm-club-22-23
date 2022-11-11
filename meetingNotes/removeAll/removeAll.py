# James Taddei
# Remove All
# 11/11/22

def main():
    # Variable declaration
    list1 = [5, 20, 15, 20, 25, 50, 20]
    list2 = list1.copy()

    # Remove All Instances of 20
    removeAllRemove(list1, 20)
    print(list1)
    removeAllPop(list2, 20)
    print(list2)

def removeAllRemove(lst: list, toBeRemoved: int) -> None:
    """
    Removes all instances of toBeRemoved from a number list via
    the 'remove' method.
    """
    while (toBeRemoved in lst):
        lst.remove(toBeRemoved)

def removeAllPop(lst: list, toBeRemoved: int) -> None:
    """
    Removes all instances of toBeRemoved from a number list without
    using the 'remove' method.
    """
    i = 0
    while (i < len(lst)):
        if (lst[i] == toBeRemoved):
            lst.pop(i)
            continue # skip i += 1
        i += 1

main()