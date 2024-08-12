
# - Scores 91 - 100: Grade = "Outstanding" 
# 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# 
# - Scores 71 - 80: Grade = "Acceptable" 
# 
# - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


# Create an empty dictionary for storing student grades
student_grades = {}

# Loop through the keys (student names) in the dictionary
for student in student_scores:
    print(student) #here i get keys
    score=student_scores[student] #here i get values
    print(score)
    
    if score>=91:
        student_grades[student]="Grade = Outstanding"
    elif score>=81:
       student_grades[student]="Grade = Exceeds Expectations"
    elif score>=71:
        student_grades[student]="Grade = Acceptable"
    elif score<=70:
        student_grades[student]="Grade = Fail"
        
print(student_grades)        



