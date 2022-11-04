Src: https://www.101computing.net/prime-factor-tree-algorithm/

Goal: Write a Python function will output the prime factorization of an inputted number.
    Also, write a program that will test this functionality.

Relevant Information:
    * The source page asks for a whole factorization tree, you're just looking for the
      prime factors
    * Ex: 140 = 2^2 * 5 * 7
    * The easiest method is pulling off the smallest prime number the current number is
      divisible by, outputting that prime, and repeating until you reach a prime
    * You should use the isPrime function from last meeting
