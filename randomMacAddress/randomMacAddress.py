# James Taddei
# Random MAC Address
# 3/29/23

# O(1)

from random import choice

def main():
    print(randomMacAddress())

def randomMacAddress() -> str:
    """
    Generates and returns a random MAC address.
    """
    # Variable declaration
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
    lenOfAddress = 6
    lenOfNum = 2
    address = ""

    for _ in range(lenOfAddress): # Runs for every hexa number
        for _ in range(lenOfNum): # Runs for each digit in the number
            address += choice(digits)
        address += ":"

    return address[:-1] # removes the last added ":"

main()