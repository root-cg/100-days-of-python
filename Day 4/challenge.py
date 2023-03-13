# coin Toss
# import random

# coin_toss = random.randint(0, 1)


# if coin_toss == 1:
#     print("Heads")
# else:
#     print("Tails")


# Banker Roulette
import random

names_string = input("Give me everybody's names, seperated by a comma. :)")
names = names_string.split(", ")
payer = len(names)
rand_name = random.randint(0, payer-1)

final_payer  = names[rand_name]
print(final_payer +" is going to buy the meal today!")
