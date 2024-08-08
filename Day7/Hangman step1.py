#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
choosen_word=random.choice(word_list)
print(choosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("Please guess a letter \n").lower()
print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in choosen_word:

    if guess==letter:
        print("Right")
    else:
        print("Wrong")
        

#Step2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
        
display=[]

for letter in choosen_word:
    display+= "_"
    print(display)
        
        
        
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for display in choosen_word:
    if letter==display:
       display=letter
       print(display)
    
        
        
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.        

        
    


