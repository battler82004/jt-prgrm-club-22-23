# James Taddei
# Good Luck
# 10/12/22

# User input
K = input("Enter a 3-digit number: ")
K = K.zfill(3)

# Order numbers
if ((K[0] <= K[1]) and (K[0] <= K[1])): # 0 is smallest
    minimum = K[0]
    if (K[1] <= K[2]): # 2 is largest
        mid = K[1]
        maximum = K[2]
    else: # 1 is largest
        mid = K[2]
        maximum = K[1]
elif ((K[1] <= K[0]) and (K[1] <= K[2])): # 1 is smallest
    minimum = K[1]
    if (K[0] <= K[2]): # 2 is largest
        mid = K[0]
        maximum = K[2]
    else: # 0 is largest
        mid = K[2]
        maximum = K[0]
else: # 2 is smallest
    minimum = K[2]
    if (K[0] <= K[1]): # 1 is largest
        mid = K[0]
        maximum = K[1]
    else: # 0 is largest
        maximum = K[1]
        mid = K[0]

# Calculations
x = minimum + mid + maximum
y = maximum + mid + minimum
z = mid + mid + mid
luckyNum = int(x) + int(y) - int(z)

# Final output
print(f"Good luck: {luckyNum}")