name= input("What is your name?") #here name is variable, where the data i will give to the input prompt will be stored in name

print ("My name is " + name)


name= "Don hu ma"
print(name)

length=len(name)
print("the length of the name is " + str(length))


# Variables
# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise

glass1="milk"
glass2="juice"

glass3=glass1 ##we made a new variable and stored glass1 value to glass3

glass1=glass2
glass2=glass3 # here we get glass1 value from varibale glass3

print(glass1)
print(glass2)
