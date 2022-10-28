# James Taddei
# Review Meeting 5
# 10/28/22

def main():
    meeting1()
    meeting2()
    meeting3()
    meeting4()

def meeting1():
    # Ints, floats, bools, chars, strings
    i = 7_200_00 # integer, int()
    f = 2_110.100 # float, double, float()
    b = True # boolean, bool()
    c = 'Q' # char, chr()
    s = "hello world!" # string, str()
    print(type(f))

    print()

    # Types don't mix
    # print("Hello " + 5) # causes error, doesn't know what you want
    print(f"Hello {5}") # only in Python 3

    print()

    # Math Operators
    print(5 // 3) # floor division (divides then rounds down)
    print(5 % 3) # modulus, remainder in division
    print(5 ** 3) # exponent
    from math import sqrt
    print(sqrt(5))

    print()

    # Comparison
    print(3 <= 5)
    print(3 == 5)
    print(3 != 5)
    print(True and False)
    print(False or True)
    print(not(True))

    print()

def meeting2():
    # If
    b = True
    if (b):
        print("True")
    
    print()

    # If Else
    if (not(b)):
        print("True")
    else:
        print("False")

    print()

    # Elif
    i = 3
    if (i == 1):
        print("True")
    elif (b == 3):
        print(i)
    else:
        print("False")

    print()

def meeting3():
    string = "Hello world!"

    # Indexing
    print(string[0:3])
    print(string[::-1])

    print()

    # Methods
    print(string.upper())
    print(string)
    string = string.upper()
    print(string)

    print()

    # Escape Chars
    string = "Hello\tWorld!"
    print(string)

    print()

    # While Loop
    while (len(string) < 20):
        string += "_"
    print(string)

    print()

    # For Loop
    for i in range(7):
        print(i)

    print()

def meeting4():
    string = "Hello"
    def myFunc(var: str = "test") -> str:
        print(string) # can access global
        print(var)
        funcVar = 32
        return var*2

    print(myFunc("World"))
    print()
    # print(funcVar) # can't access function var
    print(myFunc(string))
    print()
    print(myFunc())

main()