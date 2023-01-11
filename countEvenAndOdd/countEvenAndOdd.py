# James Taddei
# Count Even and Odd
# 1/4/23

def main():
    list1 = [2, 7, 5, 64, 14]
    list2 = [12, 14, 95, 3]

    countEvenAndOdd(list1) # Expected: 3, 2
    countEvenAndOdd(list2) # Expected: 2, 2

def countEvenAndOdd(lst: list) -> None:
    even = 0
    odd = 0

    for val in lst:
        if (val % 2 == 0):
            even += 1
        else:
            odd += 1

    print(f"Even = {even}, Odd = {odd}")

main()