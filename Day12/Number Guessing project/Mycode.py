from art import logo
import random


print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
random_number=random.randint(1, 101)
print(random_number)
ask_level=input("Choose a difficulty. write 'easy' or 'hard' ").lower()



def easy_level():
    easy = [10]
    print(f"You have 10 attempts remaining to guess the number.")
    for attempts in easy:
        # print(attempts)
        should_continue = True
        while should_continue:
            guess = int(input("Make a Guess"))
            if guess == random_number:
                print(f"WOW! You guess correct number: {random_number} in {attempts - 1} attempt left")
                return "win"
            if guess != random_number:
                attempts -= 1
            if guess > random_number:
                print("Too High")
            if guess < random_number:
                print("Too Low")
            if attempts > 1:
                print("Guess Again")
            print(f"You have {attempts} attempts remaining to guess! ")
            if attempts < 1:
                should_continue = False
                print("You Lost")


def hard_level():
    easy=[5]
    print(f"You have 5 attempts remaining to guess the number.")
    for attempts in easy:
        # print(attempts)
        should_continue = True
        while should_continue:
            guess = int(input("Make a Guess: "))
            if guess == random_number:
               print (f"WOW! You guess correct number: {random_number} in {attempts-1} attempt left")
               return "win"
            if guess != random_number:
                attempts-=1
            if guess > random_number:
                print("Too High")
            if guess < random_number:
                print("Too Low")
            print(f"You have {attempts} attempts remaining to guess! ")
            if attempts > 0:
                print("Guess Again")
            if attempts<1:
                should_continue = False
                print("You Lost")







            # guess_again=True
            # while guess_again:
            #     print("guess again")
            #     if attempts<1:
            #         guess_again=False





if ask_level=='easy':
    easy_level()

if ask_level!='easy' and ask_level!='hard':
    print("You have choose invalid option")

if ask_level=='hard':
    hard_level()


















