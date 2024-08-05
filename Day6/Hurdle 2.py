def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()  
    turn_left()

    
#using for loop    
#for steps in range(6):
    #jump()
 

# using while loop
number_of_hurdles=6
while number_of_hurdles>0:
    jump()
    number_of_hurdles-=1
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
