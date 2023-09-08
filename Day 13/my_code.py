from art import logo, vs
from ala_hota import data
import random


print(logo)
count = True
current_score = 0
not_same=[]
def checker():
    global current_score
    global choice_A
    global choice_B
    choice_A = random.choice(data)
    choice_B = random.choice(data)
    if choice_A['follower_count'] == choice_B['follower_count']:
            choice_B = random.choice(data)
    def again(): 
            """ Prassana Diamond bhau debugged code and helped me """ # same pair nahi aana chahiye aaisa hai
            print("hii")
            if len(not_same)==0:
                fst=choice_A['name']
                snd=choice_B['name']
                add=fst+"-"+snd
                not_same.append(add)
                
            else:
                fst=choice_A['name']
                snd=choice_B['name']
                add=fst+"-"+snd
                addsnd=snd+"-"+fst
                print(str(not_same)+"vs"+add)
                if add and addsnd not in not_same:
                    not_same.append(add)
                else:
                    print("Debugged++++ aala hota")
                    again()
    print(not_same)
    again()
    
    print(f"Compare A: {choice_A['name']}, {choice_A['description']}, {choice_A['country']} ")
    print(vs)
    print(f"Against B: {choice_B['name']}, {choice_B['description']}, {choice_B['country']} ")
    ask_user = input("Who has followers? type 'A' or 'B' ").capitalize()

    check_A = choice_A['follower_count'] > choice_B['follower_count']
    check_B = choice_A['follower_count'] < choice_B['follower_count']  
    print(str(choice_A['follower_count'])+">"+ str(choice_B['follower_count']))
    print(check_A)
    print(check_B)

    if check_A == True and ask_user == 'A':
        current_score += 1
        print(f"You're right ! Current Score : {current_score}")
        return current_score
    elif check_B == True and ask_user == 'B':
        current_score += 1
        print(f"You're right ! Current Score : {current_score}")
        return current_score
    else:
          print(f"Sorry, that's wrong, Final score: {current_score}")
          return 0

    # print(choice_B)





while(count):
    
    check=checker()
    if check == 0:
        count = False

