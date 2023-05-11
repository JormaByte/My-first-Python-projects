name = input("Type your name")
print("Welcome", name, "to your adventure!")

answer = input("You were walking on a dirt road and it has gone to an end. Now you must choose if you want to go left or right.. ").lower()

if answer == "left":
    answer = input("You have traveled to a river. You can walk around it, or swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator!")
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died.")
        
    else:
        print("Are you illiterate!?")

elif answer == "right":
    answer = input("You came to a brigde. Do you want to cross it or go back?")

else:
    print("Are you illiterate!?")