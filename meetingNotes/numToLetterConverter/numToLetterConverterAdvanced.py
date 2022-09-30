alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = int(input("Enter num: "))
num -= 65

if (num < 0):
    print("Num too small")
elif (num > 25):
    print("Num too big")
else:
    print(alphabet[num])