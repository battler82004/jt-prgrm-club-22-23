# Team #9 (James Taddei, Jonathan Duffy, Ethan Ruch, Jayden Lawrence)
# Question 7 (ACM Code Jam, DeSales University)
# 12/20/22

"""
FINISHED AFTER COMP

Description: This program acts an odometer for all different number base systems. The program
takes in the base value (base 10), number of digits for the odometer (base 10), initial reading
(base specificied earlier), and number of increments (base 10). The odometer is incremented by
1 the number of times inputted above. Each increment should be outputted as a specified base
number with the correct number of digits (may need leading zeros). All of this is done repeatedly
until the user simply inputs -1. 
"""

from math import floor

def main():
    outputs = []

    inn = input()
    while (inn != "-1"):
        base, digits, init, increments = inn.split()
        base = int(base)
        digits = int(digits)
        increments = int(increments)

        # From when we misunderstood the question
        # increments = connverter(increments, base)
        odo = init
        for _ in range(increments):
            odo = plus(odo, base, digits, outputs)
        
        inn = input()

    print()
    for output in outputs:
        print(output)

# Very edited after comp
def plus(val, base, digits, outputs, shouldPrint=True):
    val = str(int(val) + 1)
    if (str(base) in val):
        val = plus(val[:-1], base, digits, outputs, False) + "0"

    valCopy = val
    if (shouldPrint):
        val = (digits - len(val))*"0" + val
        outputs.append(val)

    return valCopy

# Written during comp, unecessary for problem
# def connverter(num, base):
#     final = ""

#     vals = [1]
#     last = 1
#     while (last < num):
#         last *= base
#         vals.append(last)
#     vals.reverse()

#     for val in vals:
#         if (val > num):
#             final += "0"
#         else:
#             final += str(num // val)
#             num = num % val

main()