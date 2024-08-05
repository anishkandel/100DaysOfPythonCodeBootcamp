#Escape Maze- Final Project of Day6

def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    if right_is_clear():
       turn_right()
       move()
    elif front_is_clear():
       move()
    elif wall_in_front():
        turn_left()

        
#NOT completed , i will return back after day 15         
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
