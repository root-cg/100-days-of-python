# Treasure Island

print(r"""
____...------------...____
_.-"` /o/__ ____ __ __  __ \o\_`"-._
.'     / /                    \ \     '.
|=====/o/======================\o\=====|
|____/_/________..____..________\_\____|
/   _/ \_     <_o#\__/#o_>     _/ \_   \
\_________\####/_________/
|===\!/========================\!/===|
|   |=|          .---.         |=|   |
|===|o|=========/     \========|o|===|
|   | |         \() ()/        | |   |
|===|o|======{'-.) A (.-'}=====|o|===|
| __/ \__     '-.\uuu/.-'    __/ \__ |
|==== .'.'^'.'.====""")


print("Welcome to Treasure Island")
print("Your Mission is find the treasure")

guess = input("where you want to go from entrance of this Dimention?  Right or left \n")

if guess.lower() == 'right':
    print("""Fall into a hole.
          Game Over.""")
elif guess.lower() == 'left':
    guess_2 = input("Swim in to this Dimention or wait for Boat!!....swim or wait \n")
    if guess_2.lower() == "swim":
        print("Attacked by pirana fish and unknows ghosts which are swiwmming from eternity.... Game Over...")
    elif guess_2.lower() == 'wait':
        print("There is a Door .....Opening for Your Real world...Choose the Door  ")
        guess_3 = input(" Red or Blue or Yellow \n")
        if guess_3.lower() == "red":
            print("Burned by cosmic lights ....Died ")
        elif guess_3.lower() == "blue":
            print("Eaten by Unknown crawling creatures.... Died")
        elif guess_3.lower() == "yellow":
            print("Opening the Door To Your Real world........:) You won my Boi with Some Powers ")
        else:
            print("Game Over.....")
    else:
        print("Game Over.....")
else:
    print("Game Over.....")

