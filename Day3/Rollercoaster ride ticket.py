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
    
    