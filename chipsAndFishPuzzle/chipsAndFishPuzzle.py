# James Taddei
# Chips and Fish Puzzle
# 9/23/22

# Question Source: https://www.101computing.net/the-fish-and-chips-puzzle/

# Variable declaration
a = "chips"
b = "fish"

# Switching 'a' and 'b' via a temp variable ('c')
c = a
a = b
b = c

print(a + " and " + b)