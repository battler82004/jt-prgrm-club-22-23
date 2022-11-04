# James Taddei
# caseCalc Function
# 10/21/22

def main():
    # Variable declaration
    string = "Hello WorlD!"

    # Output
    lower, upper = caseCalc(string)
    print(f"Number of lower: {lower}\nNumber of upper: {upper}")

def caseCalc(string: str) -> tuple:
    """
    Returns a tuple holding the number of lower and uppercase letters
    in string.
    """
    lower = 0
    upper = 0

    for letter in string:
        if letter.islower():
            lower += 1
        elif letter.isupper():
            upper += 1

    return (lower, upper)

main()