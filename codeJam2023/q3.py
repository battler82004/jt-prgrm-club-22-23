# Team #9 (James Taddei, Jonathan Duffy, Ethan Ruch, Jayden Lawrence)
# Question 3 (ACM Code Jam, DeSales University)
# 12/20/22

"""
Description: This program takes in n points and finds and outputs the pair with the largest
distance between them.
"""

from math import sqrt

n = int(input("Enter n: "))
points = []
maxDist = 0
maxPoints = []

for i in range(1,n+1):
    x = int(input(f"Enter x{i}: "))
    y = int(input(f"Enter y{i}: "))
    points.append([x, y])

for point1 in points:
    for point2 in points:
        d = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        if (d > maxDist):
            maxDist = d
            maxPoints = [point1, point2]

print(f"Farthest points: ({maxPoints[0][0]}, {maxPoints[0][1]}) and ({maxPoints[1][0]}, {maxPoints[1][1]})")