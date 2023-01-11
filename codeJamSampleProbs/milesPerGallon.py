# James Taddei
# Miles Per Gallon (Code Jame Sample Probs #1)
# 12/9/22

"""
Prompt:
Assume that you currently drive an older car that drives 10 miles per gallon of gas.
Given the estimated miles you would drive per year with a new car and the mpg for the
new car, determine the estimated savings in gas expenses. Prompt the user for the expected
gasoline price, the miles, and mpg for the new car. Display the estimated savings.
"""

def main():
    oldMPG = 10

    gasPrice = float(input("Enter cost of gas: "))
    numOfMiles = float(input("Enter number of miles: "))
    newMPG = float(input("Enter new mpg: "))
    
    oldGasGallons = numOfMiles / oldMPG
    oldGasCost = oldGasGallons * gasPrice

    newGasGallons = numOfMiles / newMPG
    newGasCost = newGasGallons * gasPrice
    savings = round((oldGasCost - newGasCost), 2)

    print(f"Estimated savings per year: {savings}")

main()