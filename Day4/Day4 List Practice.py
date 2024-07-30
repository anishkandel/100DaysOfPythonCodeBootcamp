states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


print(states_of_america[0]) # here we are printing the first item of the list

print(states_of_america[1]) #here we are printing the second item in the list

print(states_of_america[-1]) #here -1 means last item in the list

states_of_america[3]= "Old Jersey" # here we are changing the item in the list

print(states_of_america[3])


##APPEND function
#lets us append function, which will add the item at the end of the list

states_of_america.append("AnishYork") # here we are adding the single item at the end of the list

print(states_of_america)

#Extend Function, it will add the list at the end of the list

states_of_america.extend(["Anish Newyork", "Anish York", "Shree York", "Kandel York"])

print(states_of_america)

print(len(states_of_america))
print(states_of_america[49])


#Split() function is used to split the string into a list
names_string=input("Tell me the names of the people who are going to pay the bill?")  #here we are taking the input on string from the user
names=names_string.split(",") #here we are splitting the string into a list
print (names)




#**********************IndexError and working witn Nested Lists**************************

# print(states_of_america[55]) # here we get IndexError because we are trying to access the item which is not in the list

num_of_states = len(states_of_america) #here we will get 55 as we have 55 states here, it will not count form 0 
print(num_of_states)
# print(states_of_america[num_of_states])  #here we get IndexError because we are trying to access the item which is not in the list
print(states_of_america[num_of_states-1]) #here we did num_of_states-1 because we want to access the last item in the list



#*************************Nested Lists***************************

#let's say we have a list of fruits and vegetables, and we want to store them in a single list

fruits= ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches" ]
vegetables=[ "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen=[fruits, vegetables] #here we are creating a nested list
print(dirty_dozen)

print(dirty_dozen[1][1])
print(dirty_dozen[0])
print(dirty_dozen[1])
print (dirty_dozen[1][2])
print(dirty_dozen[1][3])


#what is 2D list? #2D list is a list of lists. 
#2D list example: fruits["apple" , "banana"] and vegetables["tomato", "potato"]]

fruits=["apple", "banana", "pears"]
vegetable=["tomato", "cauli","potato"]
meat=["chicken", "beef", "fish"]

food=[fruits, vegetable, meat]
print(food)





line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? such as A1, B2, C1, C3 \n") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter=position[0].lower() #here the input of 1st index is saved in var letter
print(letter)

abc=["a", "b", "c"]

#letter_index=abc.index(letter)

letter_index=abc.index(letter)  #so here we are finding the index of the letter in the abc list, index function will give the index of the item in the list
print(letter_index)

number_index=int(position[1])-1 #here we are finding the index of the number in the position list
print("number_index") 

map[number_index] [letter_index]="X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")




line1 = ["⬜️","⬜️","⬜️","⬜"]
line2 = ["⬜️","⬜️","⬜️","⬜"]
line3 = ["⬜️","⬜️","⬜️","⬜"]

#first we have to combine these list in a list (nested list or 2D list)
map=[line1, line2, line3]

#ask user to input for the spot
position=input("where you want to make spot like A1, B2, D1, C3?")

#let's find the index of first letter of input given by the user and use lower function
letter=position[0].lower()

#we made a list of letter abcd to find the index 
abcd=["a", "b", "c", "d"]

#we are find the index of abcd
letter_index=abcd.index(letter)
print(letter_index) #here we got index of first input


#let's find out the number index

number_index=int(position[1])-1 #becaause list starts with 0 index, we have to subtract by -1
print(number_index) #here we got number index in integar


map[number_index][letter_index] = "X" #here we replace the input item and changing the value to X

print(f"{line1}\n{line2}\n{line3}")
