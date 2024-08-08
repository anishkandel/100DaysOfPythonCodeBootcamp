import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
# Create an empty String called placeholder.
placeholder = " "
word_length=len(chosen_word)
# For each letter in the chosen_word, add a _ to placeholder
# So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = " "

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)

