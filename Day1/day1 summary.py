# Write your code below this line 👇
# print("Hello world!")
# Python is programming language create dby guido van Rossum, 1991

 # What python can do
 #used on a server to create web applications.
 #used aLONGSIDE SOFTWARE TO CREATE workflows,
 #can connect to database systems
 #can read and modify files
 #handle big data and perform complex maths
 #used for rapid prototyping, or for production-ready software development
print("hello world! \nhello world\nhello world") #new line
#Concatinate with two strings by "+"

print("hello " + "coder")
print ("hello" + " " + "Anish")

#Working with variables in python:
#lsdfj
# '''Indentation is very very important in python, which indicate a block of code
# such as loop, conditionals and functions
# '''
# print("hello" + " " + "coders) #Syntax Error
#      print("hello" + " " + "coders") #Indentation error


#inputs on Python
# input() fucntion #collect user input and use it within your code

name=input("What is your name?")
print("Hello!" + name)

#python vairables

# Varaibles are containers, for storing data values.
# name="Dego"
# name=input("What is your name?") #Dego
# a = 6 # a is of type integar
# b="xc naskjdchjks" #b is type of string
#
# #casting
#
x=str(3) #now x will be '3'
print(x)

y=int('3')
print(y)

#
print(type(x))
print(type(y))


glass1="milk"
glass2="juice"

glass3=glass1
glass1=glass2
glass2=glass3

print("glass1:" + glass1)
print("glass2:" + glass2)

#challenge is to swap the value of glass1 and glass2 variables

#variables names are case sensative
a=4
A="dego"
print(A)
print(a)

#Assign multiple Values
x, y, z= "apple", "banana", "orange" #allows us to asssign multiple vcalues to muliple variables in one line

# #one Value to multiple Variables
a=b=c="Apple"

# Unpack collection
fruits=['apple', 'banana','orange']
jake, dego, bitch= fruits #extract the values into variables
print(jake)
print(dego)
print(bitch)

#
# Output Variables
#
# print()
#
c="Python "
d="is "
e="Awesome"

print(c, d,e) #we can output multiple variables
#
# we can also use the "+" operator to output the multiple variables (strings) but not for numbers
# print(x +y+z)
#
# a=1
# b=2  
# c=3
# print(a+b+c)


#global variables
# created outside of the function

x="awesome" #x is global variable

def dego():
    print("Python is "+ x)
dego()

#Local Variables
'''if we create a variable with the same name inside a func , 
it will be local & can only be used inside the function'''

def dego():
    x="easy"
    print("Python is "+ x)
dego()

print("Python is " + x)


#Final Project Day1
print("Welcome to the Band Name Generator.")
city=input("What's the name of the city you grew up in? \n")
pet=input("What's your pet's name?\n")

print("Your band name could be " +city+ " " +pet)
