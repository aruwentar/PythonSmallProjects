import random


def roll_die():
    random.seed()
    dice_roll = random.randint(1, 6)
    print("Result of your roll is %d." % dice_roll)

def main():
    while True:
        roll_die()
        cont = input("Do you want to roll another die? [Y/N]")
        if cont == 'Y':
            pass
        elif cont == 'N':
            break
        else:
            cont = input("Invalid input!\nDo you want to roll another die? [Y/N]")
    

if __name__ == "__main__":
    main()