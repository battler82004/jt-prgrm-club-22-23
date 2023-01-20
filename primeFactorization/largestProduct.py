# James Taddei
# Largest Product
# 1/20/23

def main():
    lst = [[2, 5], [-3, 6], [4, 4], [2, 3], [83, 1], [7, 1]]
    print(largestProduct(lst))

def largestProduct(lst: list) -> list:
    """
    Returns the sub-list in the inputted 2D array with the
    largest product.
    """
    maxProduct = 0
    maxList = []
    for subList in lst:
        product = subList[0] * subList[1]
        if (product > maxProduct):
            maxList = subList.copy()
            maxProduct = product
    
    return maxList

main()