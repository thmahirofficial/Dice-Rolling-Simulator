
import random

def roll_dice():
    dice = random.randint(1, 6)
    print("You rolled a", dice)
    
while True:
    answer = input("Do you want to roll the dice? (yes/no)")
    if answer == "yes":
        roll_dice()
    elif answer == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

