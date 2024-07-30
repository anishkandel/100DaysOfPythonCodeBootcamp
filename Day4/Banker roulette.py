# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.


names_string=input("Tell me the names of person who are going pay the bill?") #here we are taking the input on string from the user
names_list=names_string.split(",") #here we are splitting the string into a list

import random

#Get the total number of items in list
num_items=len(names_list) # we have to remember that len function can't work in string, so we converted string to list
print(f"there are total 4 people {num_items}")

#Generate random numbers between 0 and the last index
#imp thing to remember is in list starts with 0 index so, we did num_items-1 below

random_choice=random.randint(0, num_items-1)

print(f" We get the index number {random_choice}")

#we use random.randint() function to randomize the int

#choose and print a random name

print(names_list[random_choice] +" is going to buy the meal today!")