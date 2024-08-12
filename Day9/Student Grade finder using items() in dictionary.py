student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades={}

for student, score in student_scores.items(): # Using .items() to iterate over both keys and values
    print(f"{student} scored {score}")
    
    if score>=91:
        student_grades[student]="Outstanding"  #adding key as [student] and value as "outstanding in "student_grades" dictionary
    elif score>=81:
        student_grades[student]="Exceeds Expectation"
    elif score>=71:
        student_grades[student]="Acceptable"
    elif score<=70:
        student_grades[student]="Fail"
        
        
print(student_grades)

for student, grades in student_grades.items():
    print(f"{student} scores {grades}")
    
    