# James Taddei
# Estimate Square Root
# 3/29/23

# O(1)

def main():
    print(estimateSquareRoot(2))
    print(estimateSquareRoot(4))
    print(estimateSquareRoot(82))

def estimateSquareRoot(num: int) -> float:
    """
    Returns an estimate square root of the number via the
    Babylonian approximation method.
    """
    x = 1
    iterations = 100
    for _ in range(iterations):
        x = (x + (num / x)) / 2

    return x

main()