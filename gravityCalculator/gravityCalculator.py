# James Taddei
# Gravity Calculator
# 9/30/22

# x(t) = 0.5 * at^2 + vi*t + xi
# Correct ans: x(10) = -490.5 m

# Variable declaration
gravity = -9.81 # m/s^2, a
initialVel = 0 # m/s, vi
time = 10 # s, t
initialPos = 0 # m, xi

# Calculations and output
finalPos = 0.5 * gravity * (time ** 2) + initialVel * time + initialPos
print(f"The object's position after {time} seconds is {finalPos} m.")