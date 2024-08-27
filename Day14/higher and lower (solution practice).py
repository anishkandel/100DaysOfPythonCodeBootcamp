# Print Logo
from art import logo, vs
from game_data import data
# choose the random data using. random.choice()

import random


# print(compare_a)
# print(compare_b)

#Get the account from data and return in print format
#as repeating the same code for two time for compare and compareB, we can define a function and return the value

def account_format(account):
    account_name=account['name']
    account_desc=account['description']
    account_country=account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess=='a'
    else:
        return guess=='b'

print(logo)
score=0
# compare_a=random.choice(data)
# print(compare_a)

compare_b=random.choice(data)

# make the guess repeatable using while loop
should_continue=True
while should_continue:

    # if both random question is same, then again generate random question
    compare_a=compare_b
    compare_b=random.choice(data)

    if compare_a == compare_b:
        compare_b = random.choice(data)

    print(f"Compare A: {account_format(compare_a)}")
    print(vs)
    print(f"Against B: {account_format(compare_b)}")
    # account_name=compare_a['name']
    # account_desc=compare_a['description']
    # account_country=compare_a['country']
    # print(f"Compare A: {account_name}, a {account_desc}, from {account_country}")
    #
    # print(vs)
    #
    # account_name=compare_b['name']
    # account_desc=compare_b['description']
    # account_country=compare_b['country']
    # print(f"Against B: {account_name}, a {account_desc}, from {account_country}")


    # ask the user to guess
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()

    # we have to clear the screen from guess input of previous but show the logo
    print('\n' * 20)
    print(logo)


    #check the answer correct or not
    ##get the followers count of each account
    followers_count_a=compare_a["follower_count"]
    followers_count_b=compare_b["follower_count"]


    #use if statement to check the answer is correct
    is_correct=check_answer(guess, followers_count_a, followers_count_b)

    #show the feedback of right and wrong and keep update the score
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue=False

    #keep score
    ##clear the screen




# make sure if answer is correct put the question b to position of a







