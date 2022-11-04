# [Author]
# Prime Factorization Outline
# 11/4/22

def main():
    primeFactorization(140) # Expected: 2*2*5*7
    primeFactorization(150) # Expected: 2*3*5*5

def primeFactorization() -> None:
    """
    Outputs the prime factorization of the inputted integer.
    If the number is <=1, the program will output an error.
    """
    pass

def isPrime(num: int) -> bool:
    """
    Returns the bool of whether the inputted number is prime.
    """
    if (num == 1): # 1 is not a prime
        return False
    for i in range(2,num):
        if (num % i == 0):
            return False # composite
    return True # prime

main()