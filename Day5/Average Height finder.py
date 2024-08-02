# Input a Python list of student heights
student_heights = input("Give your student's height").split()

# number_of_students =len(student_heights)
# 
# print(f"number of students are :{number_of_students}")


for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


total_height=0
for height in student_heights:
  total_height += height
print(f"total height is {total_height}")


number_of_students=0
for student in student_heights:
    number_of_students+=1
 number_of_students+=1
>>>>>>> ba378c6 (Day7 Hangman Game)
print(f"number of students ={number_of_students}")

average_height=round(total_height/number_of_students)
print(f"average height =: {average_height}")


