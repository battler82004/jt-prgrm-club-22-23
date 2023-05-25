# James Taddei
# Splotvian Cuisine (HSPC 2019 #4)
# 5/19/23

def main():
    """
    Outputs a Splotvianized menu to the user. The new menu is
    a modified version of an inputted menu. The program take
    each item on a line until "DONE" is inputted.
    """
    menu = enterMenu() # user inputs
    print("\nOUTPUT:")

    # Splotvianizes then outputs each item
    for item in menu:
        if (item[0].lower() == 'q'):
            print(item)
        else:
            print(f"{item} and chips")

def enterMenu() -> list:
    """
    Allows the user to keep inputting menu items on each line
    until DONE is entered.
    """
    menu = []
    item = ""
    print("INPUT:")
    while (item != "DONE"): # takes inputs until DONE
        item = input("")
        menu.append(item)

    return menu[0:-1] # removes DONE

main()