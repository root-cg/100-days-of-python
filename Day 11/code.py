from art import logo
import random
print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6,
              7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

continue_work = True

def calculate_score(cards):
        # for total in cards:
        #     if total == 11:
        #         # if sum(cards) > 21:
        #         #     return 0
        #         cards[total] = 1
        #         if sum(cards) > 21:
        #             return "no"
        #         else:
        #             return "yes"
        # return "no"
        if sum(cards) == 21 and len(cards) == 2:
            return 0  # black jack 
        


def calculate_value(cards):

    for i in range(1):
        cards.append(deal_card())
    
    if sum(cards) == 21:
        return "win"
    
    else:
        if sum(cards) > 21:
            user_cards_card=calculate_score(cards)
            if user_cards_card == "no":
                # print("Lose")
                return "lose"
            elif user_cards_card == "no":
                # print("Lose")
                return "lose"


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)

if sum(computer_cards) == 21:
    print("Dealer wins")
elif sum(user_cards) == 21 and sum(computer_cards) != 21:
    print("User wins")
    breakpoint

else:
    if sum(user_cards) > 21:
        user_cards_card=calculate_score(user_cards)
        if user_cards_card == "lose":
            print("Lose")
        elif user_cards_card == "lose":
            print("Lose")
        elif user_cards_card == "win":
            ask_inp = input("do you want another card? ")
            if ask_inp == "yes":
                another_var = calculate_value(user_cards)
            else:
                comp_var = calculate_value(computer_cards)
                if comp_var > 21:
                    print("win by computer")
                else:
                    if comp_var > calculate_value(user_cards):
                        print("win by computer")
                    elif calculate_value(user_cards) > comp_var:
                        print("win by User")
                    else:
                        print("Draw")





    
    # user_total = calculate_score(user_cards)
    # computer_total = calculate_score(computer_cards)


    # for i in range(2):
    #     user_cards.append(deal_card())
    #     computer_cards.append(deal_card())

    # for j in user_cards:
    #     if user_cards[i] == 11 and user_total != 22:
    #         user_cards = 11
    #     elif user_cards[i] == 11 and user_total > 22:
    #         user_cards[i] = 1

