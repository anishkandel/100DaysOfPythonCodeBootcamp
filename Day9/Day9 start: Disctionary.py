dictionaries={
    "loop": "The action of doing something over again",
    "Bugs": "Issues or event on the program, that avoid running the program as expected ",
    "function": "A piece of code that can be use over again when we call" }

print(dictionaries)


# Retrieving a value from a dictionary
print(dictionaries["loop"]) #callingt the key loop
print (dictionaries["function"]) # calling the key function

# Adding more items to a dictionary
dictionaries["anish"]= "Anish is an Python Programmer and future data scientiest"
print(dictionaries) #here i have added another key and value in the same dictionary and printed

# Edit an item in a dictionary
dictionaries["Bugs"]="It got solved"
print(dictionaries)


# Wipe an existing dictionary
# dictionaries={} # here i have wiped out the all the old key and values on that dictionary
# print(dictionaries)


#creating and empty dictionary
empty_dictionary={}



# Loop through a dictionary

for key in dictionaries:
    print(key)
    print(dictionaries[key]) # this will print all the values of key
#this will print all our keys stored in dictionaries    