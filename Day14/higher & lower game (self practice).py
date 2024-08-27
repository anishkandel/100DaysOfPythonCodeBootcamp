# Importing necessary modules
from art import logo, vs  # Importing the logo and vs graphic from the 'art' module to be displayed in the game.
from game_data import data  # Importing the 'data' list from the 'game_data' module, which contains the entities' information.
import random  # Importing the 'random' module to generate random numbers, used for selecting random entities.

# Display the logo
print(logo)  # Printing the logo at the start of the game.

# Initialize score
score = 0  # Initializing the player's score to 0 at the start of the game.
game_should_continue = True  # A flag to control the game loop; the game continues as long as this is True.
compare_b = random.randint(0, 6)  # Selecting a random entity from the data list to be used as the first 'B' comparison.

# Main game loop
while game_should_continue:
    # Assigning compare_a to the previous round's compare_b
    compare_a = compare_b  # Setting compare_a to the entity used as compare_b in the previous round.
    compare_b = random.randint(0, 6)  # Selecting a new random entity for compare_b.

    if compare_a == compare_b:
        compare_b = random.randint(0, 6)  # Ensuring that compare_a and compare_b are not the same entity.

    # Display choices to the user
    print(
        f"Compare A: {data[compare_a]['name']}, a {data[compare_a]['description']}, from {data[compare_a]['country']}.")
    print(vs)  # Displaying the "vs" graphic.
    print(
        f"Compare B: {data[compare_b]['name']}, a {data[compare_b]['description']}, from {data[compare_b]['country']}.")

    # Get follower counts
    followers_a = data[compare_a]["follower_count"]  # Retrieving the follower count for compare_a.
    followers_b = data[compare_b]["follower_count"]  # Retrieving the follower count for compare_b.

    print(followers_a)  # Printing compare_a's follower count (for debugging purposes).
    print(followers_b)  # Printing compare_b's follower count (for debugging purposes).

    # Ask the user for their guess
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()  # Prompting the user to guess which entity has more followers.

    # Determine if the user is correct
    is_correct = (user_choice == 'a' and followers_a > followers_b) or (user_choice == 'b' and followers_b > followers_a)
    # Checking if the user's choice is correct by comparing the follower counts.

    if is_correct:
        score += 1  # Incrementing the score if the user guessed correctly.
        print(f"Correct! Your current score is: {score}.")

        if score == 10:
            print(f"You got all {score} correct! You complete the game")  # Congratulating the user if they correctly guess all 7 comparisons.
            game_should_continue = False  # Ending the game since the user won.
    else:
        game_should_continue = False  # Ending the game if the user guessed incorrectly.
        print(f"Sorry, that's wrong. Final score: {score}.")  # Displaying the final score after a wrong guess.

# End of the game message
print("Game over! Thanks for playing.")  # Thanking the user for playing after the game ends.
