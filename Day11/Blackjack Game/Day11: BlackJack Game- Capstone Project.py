
#TODO from hint 4: Creating a function that uses the list below to return a random card
from art import logo
import random
def deal_card():
  """returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_cards=random.choice(cards) # to get random item form list, we use .choice()
  return(random_cards)


#Hint 6 ,7,8
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:  # here we checking blackjack
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
  if u_score==c_score:
      return "Draw"
  elif c_score==0:
      return "You loose, computer has Blackjack"
  elif u_score==0:
      return "You win! , You got Blackjack"
  elif u_score>21:
      return "You loose, Score is over 21"
  elif c_score>21:
      return "You win"
  elif u_score> c_score:
      return "You win"
  else:
      return "You Lost, Computer wins"


def play_blackjack():
    print(logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        # new_card=deal_card().append(user_cards)
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

        # print(user_cards)
        # print(computer_cards)


    #hint 9
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f" Your cards:{user_cards} current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")


        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True

        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass:")

            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(f" Your final hand {user_cards} and final score {user_score}")
    print(f" Computer's final hand {computer_cards} and final score {computer_score} ")
    print(compare(user_score, computer_score))


    ask_again=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if ask_again=="y":
        print("\n" *20)
        play_blackjack()
    else:
        print("Thanks for playing Game made by Anish Shree Kandel")


ask=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
play_blackjack()


# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     print("\n" * 20)
#     play_game()
# 
# print("thank you for playing game")



















