# James Taddei
# Repeating Calculator
# 10/12/22

# Variable declaration
operations = "+-*/"

# User input
operation = input("Enter the operation (ex: '+'): ")

while (operation in operations): # If is a valid operation
    # User input pt 2 (electric boogaloo)
    num1 = float(input("Enter num 1: "))
    num2 = float(input("Enter num 2: "))

    # Final outputs
    if (operation == '+'):
        print(num1 + num2)
    elif (operation == '-'):
        print(num1 - num2)
    elif (operation == '*'):
        print(num1 * num2)
    else:
        print(num1 / num2)

    # User input pt 3
    operation = input("Enter the operation (ex: '+'): ")