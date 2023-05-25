# James Taddei
# Overlap (HSPC 2019 #6)
# 5/19/23

def main():
    num = overlap()
    if (num == 0):
        print("There is no overlap between the two intervals.")
    elif (num == 1):
        print("There is an overlap of 1 unit between the two intervals.")
    else:
        print(f"There is an overlap of {num} units between the two intervals.")

def overlap() -> int:
    """
    Returns the overlap between 2 pairs of inputted numbers.
    """
    # User input
    interval1 = input("Enter interval 1: ").split()
    interval2 = input("Enter interval 2: ").split()
    min1, max1 = int(interval1[0]), int(interval1[1])
    min2, max2 = int(interval2[0]), int(interval2[1])

    # Swap if interval2 starts later
    if (min1 > min2):
        min1, min2 = min2, min1
        max1, max2 = max2, max1

    # Determination of overlap
    if (min2 >= max1): # no overlap
        # interval2 starts after interval1 ends
        return 0
    if (max2 < max1): # total overlap
        # all of interval2 is within interval1
        return max2 - min2
    return max1 - min2 # partial overlap

main()