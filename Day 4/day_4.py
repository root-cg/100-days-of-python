# Rock Paper scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# Playing Rock Paper Scissors can be as simple as scissors cuts paper, paper covers rock, and rocks crushes scissors


# print("Let's Play Rock Paper Scissors!!")

# player_choice = input("First Your Turn: \n")

# choice = [rock, scissors, paper]


# AI_choice = random.randint(0, 2)

# if player_choice == "scissors":
#     print(scissors)
#     if choice[AI_choice] == paper:
#         print(paper)
#         print("You win!!")
#     elif choice[AI_choice] == rock or choice[AI_choice] == scissors:
#         print(rock)
#         print("Try Again")
# elif player_choice == "paper":
#     print(paper)
#     if choice[AI_choice] == rock:
#         print(rock)
#         print("You win")
#     elif choice[AI_choice] == scissors or choice[AI_choice] == paper:
#         print(scissors)
#         print("Try Again")
# elif player_choice == "rock":
#     print(rock)
#     if choice[AI_choice] == scissors:
#         print(scissors)
#         print("You win")
#     elif choice[AI_choice] == paper or choice[AI_choice] == rock:
#         print(paper)
#         print("try again")
# else:
#     print(choice[AI_choice])
#     print("Better Luck Next Time !!")



#improved the game

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")