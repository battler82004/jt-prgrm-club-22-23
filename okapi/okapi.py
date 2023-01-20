# James Taddei
# Okapi (Bloomsburg '18 #1)
# 3/10/22

def main():
    rolls = (raw_input("Enter dice rolls: ")).split()
    for roll in range(3):
        rolls[roll] = int(rolls[roll])

    if (rolls[0] == rolls[1] and rolls[1] == rolls[2]): # 3 same rolls
        print("The payout is $" + str(3*rolls[0]) + ".")
        return
    
    if (rolls[0] != rolls[1] and rolls[0] != rolls[2] and rolls[1] != rolls[2]): # no same roles
        print("The payout is $0")
        return

    # 2 same roles; since the middle roll must be the num with 2 occurrences of that roll
    rolls.sort()
    print("The payout is $" + str(2*rolls[1]))

main()
