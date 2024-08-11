# 
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# 
# number of cans = (wall height x wall width) ÷ coverage per can.
# 
# e.g. Height = 2, Width = 4, Coverage = 5
# 
# number of cans = (2 * 4) / 5
#                = 1.6

def paint_calc(height, width, cover):
   number_of_cans=math.ceil((height*width)/cover)
   print(f"You'll need {number_of_cans} cans of paint.")   

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
