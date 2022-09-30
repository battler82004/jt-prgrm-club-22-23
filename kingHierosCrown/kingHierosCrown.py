# James Taddei
# Crown Material Determiner
# 9/30/22

# User input
mass = float(input("Input the mass of the crown in kg: "))
volume = float(input("Input the volume of the crown in cubic meter: "))

# Calculation
density = mass / volume # kg/m^3

# Material selection
if ((density >= 2400) and (density <= 2700)):
  metal = "aluminum"
elif ((density >= 8100) and (density <= 8300)):
  metal = "bronze"
elif ((density >= 10_400) and (density <= 10_600)):
  metal = "silver"
elif ((density >= 11_200) and (density <= 11_400)):
  metal = "lead"
elif ((density >= 17_100) and (density <= 17_500)):
  metal = "gold"
elif ((density >= 21_000) and (density <= 21_500)):
  metal = "platinum"
else: # Density doesn't fit a known metal
  metal = "unknown"

# Final output
print("The cronw is made of: " + metal)