print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L") # What size pizza do you want? S, M, or L    
add_pepperoni = input("Do you want pepperoni? Y or N") # Do you want pepperoni? Y or N
extra_cheese = input(" Do you want extra cheese? Y or N") # Do you want extra cheese? Y or N


# Based on a user's order, work out their final bill.
# 
# Small pizza (S): $15
# 
# Medium pizza (M): $20
# 
# Large pizza (L): $25
# 
# Add pepperoni for small pizza (Y or N): +$2
# 
# Add pepperoni for medium or large pizza (Y or N): +$3
# 
# Add extra cheese for any size pizza (Y or N): +$1




bill=0

if size=="S":
 bill+=15

elif size=="M":
 bill+=20
   
else:
    bill+=25
 
 
#add cost of pepperoni
    
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
        
    else:
        bill+=3
        
        
#add cost of extra cheese
if extra_cheese=="Y":
   bill+=1
   
print(f"Your total bill is: ${bill}")   
 

# bill=0
# 
# if size=="S":
#   bill=15
#   if add_pepperoni=="Y":
#     bill+=2
#   if extra_cheese=="Y":
#     bill+=1
#     print(f"Your final bill is: ${bill}.")
#   else:
#       print(f"Your final bill is: ${bill}.")
#       
# if size=="M":
#   bill=20
#   if add_pepperoni=="Y":
#     bill+=3
#   if extra_cheese=="Y":
#     bill+=1
#     print(f"Your final bill is: ${bill}.")
#   else:
#       print(f"Your final bill is: ${bill}.")
#       
#       
# if  size=="L":
#   bill=25
#   if add_pepperoni=="Y":
#     bill+=3
#   if extra_cheese=="Y":
#       bill+=1
#       print(f"Your final bill is: ${bill}.")
#   else:
#       print(f"Your final bill is: ${bill}.")
      
      
