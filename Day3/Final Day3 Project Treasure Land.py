print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

#get input from the user asking left or right
cross_road=input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

#condition if user want to go left-print a statement and ask another input of "boat" or "swim" or if right- send to the else game over 
if cross_road=="left": 
   boat_swim=input("You've come to a lake. There is an island in the middle of the lake.\n Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
   
   #nested condition if user choose to wait for boat or swim, if user choose wait, make true and ask another input of choose color
   if boat_swim=="wait":
     color=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
     
     #nested condition under wait input to choose the colors, red, yellow or blue and print the final result
     if color=="yellow":
        print("You found the treasure! You Win!")
     elif color=="red":
        print("It's a room full of fire. Game Over.")
     elif color=="blue":
         print("It's a room full of beasts. Game Over.")
     else:
        print("You choose the door, that doesn't exist. Game Over.")
   else:
    print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")