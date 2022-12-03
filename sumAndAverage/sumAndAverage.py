# James Taddei
# Sum and Average
# 11/9/22

def main():
    numbers = [-1, 0, 1, 2, 3, 4, 5]
    total = summation(numbers)
    print(f"Sum = {total}\nAverage = {total / len(numbers)}")

def summation(lst: list) -> float:
    """
    Finds the sum of the numbers in the inputted list.
    """
    total = 0
    for num in lst:
        total += num
    return total

main()