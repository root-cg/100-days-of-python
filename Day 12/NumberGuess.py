from art import logo 
import random 
print(logo)

number_in_between = True
random_number = random.randrange(1,100)
easy = 10
hard = 5
guess_input = int(input("Guess the Number between 1 to 100: "))
guess_level = input("Choose the level: 'easy' or 'hard' level ").lower()

if guess_level == 'easy':
     guess_level = easy
elif guess_level == 'hard':
     guess_level = hard

while(number_in_between):
    if guess_input  <= 100 and guess_input >= 1:
        number_in_between = False




def guess_checker(random_number, guess_input):
        if guess_input > random_number:
            print("Too high")
        elif guess_input < random_number:
            print("Too low")
        elif guess_input == random_number:
            print("You won")
            return 0

for _ in range(guess_level):
    win_status = guess_checker(random_number,guess_input)
    print(random_number)
    print(_)
    if win_status == 0:
         break
    guess_input = int(input("Guess the Number between 1 to 100: "))
    if _ == 3 and guess_level == 5:
         print("Last attempt")
    elif _ == 8 and guess_level == 10:
         print("Last attempt")
