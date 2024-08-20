from art import logo
import random


print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
random_number=random.randint(1, 101)
print(random_number)
ask_level=input("Choose a difficulty. write 'easy' or 'hard' ").lower()

def get_valid_guess(previous_guesses):
    while True:
        guess = input("Make a Guess: ")
        if guess.isdigit():
            guess = int(guess)
            if guess in previous_guesses:
                print("You've already guessed that number. Try again.")
            else:
                previous_guesses.append(guess)
                return guess
        else:
            print("Please enter a valid integer.")

def easy_level():
    attempts=10
    previous_guesses=[]
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts>0:
        guess = get_valid_guess(previous_guesses)
        if guess == random_number:
            print(f"WOW! You guess correct number: {random_number} in {attempts - 1} attempt left")
            return "win"
        elif guess > random_number:
            print("Too High")
        else:
            print("Too Low")
        attempts-=1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess! ")
        else:
            print("You Lost")


def hard_level():
   attempts=5
   previous_guesses = []
   print(f"You have {attempts} attempts remaining to guess the number.")
   while attempts>0:
      guess = get_valid_guess(previous_guesses)
      if guess == random_number:
          print (f"WOW! You guess correct number: {random_number} in {attempts-1} attempt left")
          return "win"
      elif guess > random_number:
          print("Too High")
      else:
          print("Too Low")
      attempts-=1
      if attempts > 0:
          print(f"You have {attempts} attempts remaining to guess the number.")
      else:
          print("You lost")

if ask_level=='easy':
    easy_level()

elif ask_level=='hard':
    hard_level()

else:
    print("You have choose invalid option")


















