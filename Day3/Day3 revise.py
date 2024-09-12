#Day3 revision


#Day3: Conditional Statements, logical Operators, Code blocks and Scope
##Conditional Statements (IF...Else)
"""

#python supports the usual logical conditions from mathematics

*Equals: a==b
*Not Equal: a!=b
*Less than: a<b
*Less than or equal to: a<=b
*Greater than : a>b
* Greater than or equal to : a>=b

Note: these conditions can be used in several ways, most commonly
in "If statements" and "Loops.

"""

###  IF keyword
a=32
b=150
if b>a:
    print("b is greater than a")

#Note: Indentation define scope in the code

### Elif Statement
'''
the "elif" keyword is python's way of saying-
"if the previous conditions were not TRUE, then try 
this condition"
'''
a=32
b=32
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is greater than b")

####ELSE Statement
'''
the "else" keyword catches anything which isn't caught by
preceding conditions
'''
a=200
b=20
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than a")


### IF...ELIF...ELSE
'''
if condition1:
     do A
elif condition2:
     do B
else:
     do this          
'''

### Multiple If
'''
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C        
'''

### Multiple Conditions
'''
if condition1 & condition2 & condition3:
    do this
else:
    do this    
'''

##Logical operators

'''
and    returns true if both statements are true  x<5 and x<10

or     returns true if one of the statements are true  x<5 or x<4

not    reverse the result, returns false if the result is true   not(x<5 and x<10)
'''


# Ternary operators or conditional expressions
### Short hand if

'''
if we have only onw statement to execute, we can put it on the
same line as the "if statement"
'''
##if condition: statement
if a>b:print("a is greater than b")


##Short hand IF....Else

'''
if we have only one statement to execute, 
one for IF, and one for ELSE, 
we can put it all on the same line
'''

#statement_when_true IF condition Else statement_when_false
a=3
b=20
print("A") if a>b else print("B")


he="i love you"
she="i hate you"

print("I love you") if he==she else print ('I hate you')

#We can also have multiple else statements on the same line
#statement_when_true IF condition
a=320
b=320
print("A") if a>b else print("equal") if a==b else print("B")


if a>b:
    print("A")
elif a==b:
    print("Equal")
else:
    print("B")


###  AND
'''
"and" keyword is a logical operator, and is used to 
combine conditional statements
'''
#testing if "a" is greater than "b" AND if "c" is greater than "a"
a=25
b=20
c=27

if a>b and c>a: # both conditions should be true to execute this block of code
    print(" Both conditions are true")


### OR
'''
"OR" keyword is logical operator, and it is used
to combine conditional statement
'''
#testing if "a" is greater than "b" OR if "a" is greater than "c"
a=450
b=200
c=500
if a>b or a>c: # at least 1 condition should be true
    print("At least one of conditions is TRUE")

### NOT
'''
"not" keyword is a logical operator, and is used to reverse
the result to the conditional statements
'''
# Testing if "a" is NOT greater than b

a=200
b=250

if not a>b: # True
    print("a is not greater than b")


#### Nested If...else
'''
We can have "if statements inside if" statements
which is called nested if statements.

if condition:
   if another condition:
        do this
   else:
        do this     

'''
x=25
if x>10:
    print("Above ten,")
    if x>20:
        print("also above 20")
    else:
        print("but not above 25")


#### The pass statement
'''
"if" statements cannot be empty
but if we for some reason have an "if" statement with no content,
we can jut put "pass" statement to avoid getting an error
'''
a=200
b=300
if b>a:
    pass #here having an empty "if" statement would raise error without the pass statement



###Modulo operator

a=10%5
b=10%3
#Modulo Practice

user=int(input("write a number to check Odd or Even number"))
if user%2==0:
    print(f"your number is {user} and it's even")
else:
    print(f" your number is {user} and it's odd")


#Exercise1: Pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill=0
if size=='s':
    bill+=15
elif size=='m':
    bill+=20
elif size=='l':
    bill+=25
else:
    print("choose right size Please!")

if pepperoni=='y':
    if size=='s':
        bill+=2
    else:
        bill+=3

if extra_cheese=='y':
    bill+=1
print(f' total bill is ${bill}')

# bill=0
# if size=="s":
#     bill+=15
#     if pepperoni=="y":
#         bill+=2
# if size=="m":
#     bill+=20
#     if pepperoni=="y":
#        bill+=3
# if size=="l":
#     bill+=25
#     if pepperoni=="y":
#         bill+=3
#
# if extra_cheese == 'y':
#    bill+= 1
# print(f" Your final b:ill is ${bill}")



#Excerise 2- Roller Coaster Ride
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill=0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")



#Final Project Treasure Island Project
print( r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1=='left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2=input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if choice2=='wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice3=input("One red, one yellow and one blue. Which colour do you choose?\n")
        if choice3=="blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3=="red":
            print("It's a room full of fire. Game Over.")
        elif choice3=="yellow":
            print("You found the treasure! You Win!")
        else:
            print("Please choose among 3 doors")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")





#Some importants keys
'''
What are the different types of control statements in Python?
=> In python, control statements are used to alter the flow of execution, based on specific conditions or looping 
requirements.

the main type of control statements  are:
-conditional statements: if, else, elif (Used to execute code based on certain conditions (if, else, elif).
-looping statements: for, while (used to execute repeatedly until the conditions are met)
-control flow statements: break, continue, pass, return  (commands that stops or change that how the program runs)
'''


'''
conditional statements: (if, elif, else) they check if something is true or false and
based on that, they run certain parts of the code.

control statements: these are bigger group. they include conditional statements and also things l
like loops (for, while) and commands that stops or change that how the program runs
(break, continue, return)
'''


##Some interview questions and excerise

#write a program to check weather the person is eligible for voting
age=int(input("What is your age?"))

print("you are not eligible") if age<18 else print("You are eligible") if age>=18 else print(" you choose wrong input")