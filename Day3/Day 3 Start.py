#DAY3 CONDITIONAL STATEMENTS, LOGICAL OPERATORS, CODE BLOCKS AND SCOPE



#********************CONDITIONAL STATEMENTS*************************

#Example 1
#Write a program when a user can have rollercoaster ride only if user has height of 110 and more than 100.

height= int(input("Enter your height in cm:"))
if height>=110:
  print("you can ride the rollercoaster")
else:
  print("please grow your height at least 110cm to ride the rollercoaster, Thank your for visiting!")
  
  
#Excercise 1

#Write a program to find the input number is odd or even
  
number=int(input("give me an whole number\n")) 

#let's check the number can be divided by 2 with no remainder

if number%2==0: # here % modulus is used to find remainder
 print("Your input is an even number")
else: # otherwise the number can not be divided by 0 remainder
    print("Your input is an odd number")
    
    
    
# Nested  if and elif statement
    
#Excerise 2
#Write a program to allow the user to ride rollercoaster who has height of 120 and more and
#charge the ticket price 5$ who are under 10 years, they can't particpate,5$ who are between 10 to 15
#and 7$ for 16 to 20 years old and 20$ for above years.
    
#next challenge is ask user to take a photo or not, if they say yes, charge 3$ each in their bill    
    
height= int(input("Tell us your height"))
bill=0


#let's make condition wether the height is 120 or less
if height>=120:
    print("You can ride the rollercoaster! please tell us your age for the payments")
    age=int(input("Tell us your age"))
    if age<10:
        print("sorry you can't participate" )
    elif age<=15:
        bill=5
        print("ticket for under 16 is 5$ for the entry")
    elif age<=20:
        bill=7
        print("Ticket for teens is 7$ for the entry")
    elif age>=45 & age<=55:
        bill=0
        print("Ticket for old age is $0 fro the entry")
    else:
        bill=20
        print("Ticket for adult is 20$ for the entry")
        
    photo=input("Do you want to take a photo Y or N ?")
    if photo=="Y":
     bill+=3
     
    print(f" your total bill is {bill}")
   
else:
    print("Your height is not enough to participate in rollercoaster ride, please grow your height")
    
    
    
#What is whole number? 
#Whole number is a number which is divisible by 1 and itself. such as 2,4,6,8,10,12,14,16,18,20,22,24,26, whole number are even numbers.




#Nested if/else statement
#Nested if/else statement is used to check for multiple conditions.


#count() function is used to count the number of times a letter occurs in a string.

    
    
    
    