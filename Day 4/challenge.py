# coin Toss
# import random

# coin_toss = random.randint(0, 1)


# if coin_toss == 1:
#     print("Heads")
# else:
#     print("Tails")


# Banker Roulette
# import random

# names_string = input("Give me everybody's names, seperated by a comma. :)")
# names = names_string.split(", ")
# payer = len(names)
# rand_name = random.randint(0, payer-1)

# final_payer  = names[rand_name]
# print(final_payer +" is going to buy the meal today!")


#Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# position_split = position.split()


first = int(position[0])
second = int(position[1])
map[second- 1][first - 1] = ' X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

