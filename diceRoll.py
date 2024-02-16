import random

def roll_dice():
    print("Rolling the dice..")
    return random.randint(1,6)

print("Welcome to my dice rolling simulator!")
while True:
    answer=input("Press enter to roll the dice, or press q + enter to exit..")
    if answer=="q":
        print("You quit the game")
        break
    
    dice_result = roll_dice()
    print("You rolled a", dice_result)



