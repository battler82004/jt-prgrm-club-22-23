# James Taddei
# Earths Volume in Lego Bricks
# 9/11/22

# Question Source: www.101computing/what-if-planet-earth-was-made-of-lego/

from math import pi

# Variable declaration
radiusOfEarth = 6371 * 1_000_000 # 1 km = 1,000,000 mm
legoWidth = 16 # mm
legoLength = 16 # mm
legoHeight = 10 # mm

# Calculations
volumeOfEarth = (4/3) * pi * (radiusOfEarth ** 3)
volumeOfLego = legoWidth * legoLength * legoHeight
numOfBricksNeeded = volumeOfEarth / volumeOfLego

print("Number of bricks needed:", numOfBricksNeeded)