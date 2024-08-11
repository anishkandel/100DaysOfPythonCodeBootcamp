#life Week Finder 

total_weeks=90*52

print(total_weeks)


def life_in_weeks(number):
    week_left=total_weeks-number*52
    print(f"You have {week_left} weeks left")            
life_in_weeks(20)   