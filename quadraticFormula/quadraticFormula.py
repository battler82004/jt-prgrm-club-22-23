# James Taddei
# Quadratic Formula
# 11/3/22

from math import sqrt

def main():
   quadraticForm(1, 2, -15) # Real roots of -3, 5
   quadraticForm(3, 4, 5) # No real roots

def quadraticForm(a: float, b: float, c: float) -> None:
    """
    Outputs the real roots of a quadratic equation based on the quadratic
    formula. If the roots are imaginery, it outputs the error.
    """
    discriminant = b ** 2 - 4 * a * c
    if (discriminant < 0): # Checks for complex roots
        print(f"Error, roots of {a}x^2+{b}x+{c} are imaginery.")
    else: # Roots are real
        rootOfDiscriminant = sqrt(discriminant)
        root1 = (-b + rootOfDiscriminant) / (2 * a)
        root2 = (-b - rootOfDiscriminant) / (2 * a)
        print(f"The roots of {a}x^2+{b}x+{c} are: {root1} and {root2}.")

main()