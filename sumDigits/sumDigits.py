# James Taddei
# Sum Digits
# 10/12/22

# User input
num = int(input("Enter a num: "))
ogNum = num
total = 0

# Goes until only 1 digit
while (num >= 10):
    total += num % 10 # Add ones digit
    num = num // 10 # Remove ones digit

total += num # Account for highest digit
print(f"\nThe total value of the digits of {ogNum} = {total}") # Final output