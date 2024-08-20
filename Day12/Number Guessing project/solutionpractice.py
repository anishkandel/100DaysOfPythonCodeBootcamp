from tabnanny import check

from art import logo



#choosing a random number between 1 to 100
from random import randint



EASY_LEVEL=10
HARD_LEVEL=5
INVALID_OPTION="You have chosen invalid option"
#function to user's guess against actual number
def check_answer(guess, random_number, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if guess< random_number:
        print (" Too Low")
        return turns-1
    elif guess> random_number:
        print("Too High")
        return turns-1
    else:
        print(f"You guess the right answer: {random_number}")

#function to set difficulty levels
def set_level():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL



def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = randint(1, 100)
    print(f"the correct answer is {random_number}")

    turns = set_level()
    # Repeat the guessing functionality if they get it wrong.
    guess=0
    while guess!=random_number:
        print(f" You have remaining {turns} left ")
        guess = int(input("Make a guess: "))
        #track the number of turns and reduce by 1 if user guess wrong
        turns=(check_answer(guess, random_number, turns))
        if turns==0:
            print(" You ran out of attempts, You lost")
            return
        elif guess!=random_number:
            print("Guess Again ")


game()
