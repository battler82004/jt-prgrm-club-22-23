# James Taddei
# FizzBuzz
# 10/12/22

# Variable declaration
fizzNum = 3
buzzNum = 5

for i in range(1,101):
    if (i % (fizzNum * buzzNum) == 0): # Div by both
        print("Fizzbuzz")
    elif (i % fizzNum == 0):
        print("Fizz")
    elif (i % buzzNum == 0):
        print("Buzz")
    else: # Not divisible
        print(i)