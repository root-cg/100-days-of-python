from art import logo
import os
print(logo)


print("Welcome to secret Auction program.")

should_continue = True
bid = {}


while (should_continue):
    name = input("what's your name? ")
    bid_value = int(input("whata's your bid? "))
    others = input(""" Are there any other bidders? "yes" or "no" """).lower()
    bid[name] = bid_value
    os.system('cls')

    if others == "no":
        should_continue = False



temp = 0;
for key in bid:
    if bid[key] > temp:
        temp  = bid[key]
        name_ans = key

print(f"The winner is {name_ans} with a bid of ${temp}")    