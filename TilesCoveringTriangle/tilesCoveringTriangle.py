# James Taddei
# Tiles Covering Triangle (Code Jame Sample Probs #3)
# 12/9/22

"""
Prompt:
Assume that you covering a triangular-shaped area with tiles that are 10 X 10 inches. The area
is an equilateral triangle. The tiles will be arranged in rows with one row aligned with one of
the sides. Call this side the base. The height of an equilateral triangle is .866 times the base.
The tiles are directional so that when a tile is cut to fit the slope on one edge, the remaining
piece of tiles cannot be used anywhere else. The vertical edges do not have to be aligned. Given
the length of the base, calculate the minimum number of tiles that are needed to completely cover
the area.
"""

def main():
    # Variable declaration and user input
    tileLength = 10
    triBaseLength = int(input("Enter length of a side: "))

    # Find number of tiles in base
    numOfTilesInBase = triBaseLength // tileLength
    if (numOfTilesInBase == 0):
        print("Number of tiles: 0")
        return
    if (numOfTilesInBase == 1):
        print("Number of tiles: 1")
        return

    # Calculate the total number of tiles
    numOfBoxesInTri = 0
    currWidth = numOfTilesInBase
    # Goes through each row and adds the number of boxes for the row. Each row up holds one less
    # than the last
    for i in range(numOfTilesInBase):
        numOfBoxesInTri += currWidth
        currWidth -= 1

    print(f"Number of tiles: {numOfBoxesInTri}")

main()