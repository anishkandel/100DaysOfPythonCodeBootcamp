#Password Generator Project



# Importing the random module to use its functions
import random

# Lists of characters to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Welcome message for the user
print("Welcome to the PyPassword Generator!")


# Asking the user for the number of each type of character they want in their password
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91



# Initialize an empty string for the password
#Initialize an empty list to hold the characters of the password
# An empty string password is initialized to build the password by appending characters to it.
#This method is straightforward for constructing a password where the order of character types (letters, symbols, numbers) doesn't need to be randomized.

password=""


#For each type of character (letters, symbols, numbers), a loop runs the specified number of times (provided by the user).
#In each iteration, a random character is chosen from the corresponding list and appended to the password string.


# Add the specified number of random letters to the password
for char in range(1, (nr_letters+1)):
   password+=random.choice(letters)
   
# Add the specified number of random symbols to the password
for char in range(1, nr_symbols+1):
    password+=random.choice(symbols)
    
# Add the specified number of random numbers to the password
for char in range(1, nr_numbers+1):
    password+=random.choice(numbers)
print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#An empty list password_list is initialized.
#Using a list makes it easier to randomize the order of characters later because the random.shuffle() method can directly operate on lists.

password_list=[]


#Similar to the easy level, loops add the specified number of random characters to the password_list.
# Add the specified number of random letters to the list
for char in range(1, (nr_letters+1)):
   password_list.append(random.choice(letters))
   
# Add the specified number of random symbols to the list
for char in range(1, nr_symbols+1):
    password_list+=random.choice(symbols)

# Add the specified number of random numbers to the list
for char in range(1, nr_numbers+1):
    password_list+=random.choice(numbers)
print(password_list)


# Randomize the order of characters in the list
#The random.shuffle() method randomizes the order of elements in password_list.
random.shuffle(password_list)

# Print the list after shuffling
print(password_list)

#An empty string password is initialized again, and
#the characters from the shuffled password_list are concatenated to form the final password.

password=""

# Combine all characters in the list into a single string
for char in password_list:
    password+=char
    
# Print the final randomized password   
print(f"We have generated your password {password}")    