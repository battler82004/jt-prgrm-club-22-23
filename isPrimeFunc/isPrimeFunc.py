# James Taddei
# isPrime Function
# 10/21/22

def main():
    num = int(input("Enter a num to test if it's prime: "))
    if isPrime(num):
        print(f"The number {num} is prime")
    else:
        print(f"The number {num} is not prime")

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