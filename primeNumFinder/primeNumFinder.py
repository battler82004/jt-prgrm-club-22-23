# James Taddei
# Prime Number Finder
# 10/28/22

import math

def main():
    # Uses Wilson's prime number formula
    for i in range(1,7): # Breaks at n = 7
        print(f"Prime {i} = {primeNum(i)}")

    print("\n")

    # Uses better prime number formula
    primeNums = set()
    i = 1
    # Have to use a set and check len of it beacuse this formula doesn't
    # always return a unique prime.
    while (len(primeNums) < 10): # Finds first 10 primes
        primeNums.add(betterPrimeNum(i))
        i += 1

    primeNums = list(primeNums)

    for pos, num in enumerate(primeNums, 1): # Outputs primes
        print(f"Prime {pos} = {num}")

def primeNum(n: int) -> int:
    """
    Returns the nth prime number based on Wilson's prime number formula.
    """
    outerSum = 1 # Handles the 1+
    for i in range(1, 2 ** n + 1): # Outer sum loop
        innerSum = 0
        for j in range(1, i+1): # Find inner sum
            innerSum += math.floor((math.cos((math.factorial(j - 1) + 1) * math.pi / j)) ** 2)
        outerSum += math.floor((n / innerSum) ** (1 / n))
    return outerSum

def betterPrimeNum(n: int) -> int:
    """
    Returns the a prime number based on the follow prime number formula:
        P(n) = floor((n! % (n + 1)) / n) * (n - 1) + 2

    Prime is not always unique.
    """
    return math.floor((math.factorial(n) % (n + 1)) / n) * (n - 1) + 2

if (__name__ == "__main__"):
    main()
