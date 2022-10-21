# James Taddei
# maxNum Function
# 10/21/22

def main():
    # User input
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    num3 = float(input("Enter the third num: "))

    # Output
    maximum = maxNum(num1, num2, num3)
    print(f"The max number of the three is: {maximum}")

def maxNum(num1: float, num2: float, num3: float) -> float:
    """
    Returns the vale largest of the three inputted numbers.
    """
    if ((num1 >= num2) and (num1 >= num3)):
        return num1
    elif ((num2 >= num1) and (num2 >= num3)):
        return num2
    
    return num3

main()