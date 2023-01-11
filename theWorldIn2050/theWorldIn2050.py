# James Taddei
# The World in 2050
# 1/4/23

def main():
    # Variable declaration
    population = 7_850_000_000
    year = 2022

    # Goes through each year and changes the population
    while (population < 10_000_000_000):
        population *= 1.01
        year += 1

    print(f"In {year}, the world population will be {population}")
    # Correct ans: 2047, population = 10067091160.885288

main()