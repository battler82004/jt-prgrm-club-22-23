# James Taddei
# Matchstick Display
# 3/29/23

# Optimized: O(1), unoptimized: O(n+m)

def main():
    num = int(input("Enter the number of matchsticks: "))
    print(f"In: {num}, Out: {matchstickDisplay(num)}")
    # Ex: 
    #   In: 2, Out: 1
    #   In: 6, Out: 111
    #   In: 11, Out: 71111

def matchstickDisplay(num: int) -> int:
    """
    Returns the largest number that can be displayed by a 7-segment
    dispaly with only 'num' segments (matchsticks) lit. This
    algorithm has been optimized.
    """

    if ((num == 1) or (num == 0)): # can't make a num
        print("Error! Number is too small.")
        return 0

    if (num % 2 == 0): # even number (only 1s)
        return int("1" * int(num / 2))
    
    # Odd num, 1s and a leaing 7
    return int("7" + ("1" * ((num // 2) - 1)))

def matchstickDisplayUnoptimized(num: int) -> int:
    """
    Returns the largest number that can be displayed by a 7-segment
    dispaly with only 'num' segments (matchsticks) lit.
    """
    if (num % 2 == 0): # Even number, only 1s
        return int("1" * int(num / 2))

    # Since the number is odd, numbers besides 1 will be present.
    # This removes digit and continuously subtracts one until a
    # creatable number is determined. 
    potMax = int("9" * floor(num / 2))
    total = totalLitSegments(potMax)
    while (total > num):
        potMax -= 1
        total = totalLitSegments(potMax)

    return potMax

def totalLitSegments(num: int) -> int:
    """
    Returns the total number of lit segments if a number were to
    be dispalyed on a 7-segment display.
    """
    litSegments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    strNum = str(num)
    total = 0
    for strDigit in strNum:
        total += litSegments[int(strDigit)]

    return total

main()