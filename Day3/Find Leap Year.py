#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.

#This is how you work out whether if a particular year is a leap year.

#on every year that is divisible by 4 with no remainder

#except every year that is evenly divisible by 100 with no remainder

#unless the year is also divisible by 400 with no remainder

# e.g. The year 2000:
# 
# 2000 ÷ 4 = 500 (Leap)
# 
# 2000 ÷ 100 = 20 (Not Leap)
# 
# 2000 ÷ 400 = 5 (Leap!)
# 
# So the year 2000 is a leap year.
year=int(input("give me year"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
             print("Not leap year") 
    else:
        print("Leap year")
else:
    print("Not leap year")