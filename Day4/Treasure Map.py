# line1 = ["⬜️","⬜️","⬜️","⬜"]
# line2 = ["⬜️","⬜️","⬜️","⬜"]
# line3 = ["⬜️","⬜️","⬜️","⬜"]

# #first we have to combine these list in a list (nested list or 2D list)
# map=[line1, line2, line3]

# #ask user to input for the spot
# position=input("where you want to make spot like A1, B2, D1, C3?")

# #let's find the index of first letter of input given by the user and use lower function
# letter=position[0].lower()

# #we made a list of letter abcd to find the index 
# abcd=["a", "b", "c", "d"]

# #we are find the index of abcd
# letter_index=abcd.index(letter)
# print(letter_index) #here we got index of first input


# #let's find out the number index

# number_index=int(position[1])-1 #becaause list starts with 0 index, we have to subtract by -1
# print(number_index) #here we got number index in integar


# map[number_index][letter_index] = "X" #here we replace the input item and changing the value to X

# print(f"{line1}\n{line2}\n{line3}")





import sys

# Define the map
line1 = ["⬜️", "⬜️", "⬜️", "⬜"]
line2 = ["⬜️", "⬜️", "⬜️", "⬜"]
line3 = ["⬜️", "⬜️", "⬜️", "⬜"]
map = [line1, line2, line3]

# Get position from command-line argument
if len(sys.argv) > 1:
    position = sys.argv[1]  # ✅ Get position from argument
else:
    position = "B2"  # ✅ Default value

print(f"Position selected: {position}")

# Find the index of the first letter
letter = position[0].lower()
abcd = ["a", "b", "c", "d"]
letter_index = abcd.index(letter)

# Find the number index
number_index = int(position[1]) - 1

# Replace the item with "X"
map[number_index][letter_index] = "X"

# Print the updated map
print(f"{line1}\n{line2}\n{line3}")

