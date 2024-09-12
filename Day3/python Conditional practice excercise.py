
##Some interview questions and excercise

#1) write a program to check whether the person is eligible for voting
age=int(20)

print("you are not eligible") if age<18 else print("You are eligible")


if age>=18:
    print("you are eligible")
else:
    print("you are not eligible")


print("You are eligible") if age>=18 else print("you are not eligible")



#2 write a program that is divisible by 7 or not

number=int(100)

print("number is divisible by 7") if number%7==0 else print("number is not divisible by 7")

#3 Write a program to display "hello" if the number entered by user is a multiple of 5, otherwise print "Bye"

number=int(25)

print("Hello") if number%5==0 else print("Bye")


#4 write a program to calculate the electricity bill (accept number of unit from the user) according to the following criteria

'''
first 100 units = no charge
next 100 units= rs 5 per units
after 200 units= rs 10 per units

eg: if input unit is 350 than total bill amount is rs 2000
'''

units=float(350.20)
total_bill=0
if units<=100:
    total_bill=0 #No charge for the first 100 units

#if the units are between 101 and 200
elif units<=200:
    bill=(units-100)*5 #charge rs 5 for each units beyond 100

#if the units are above 200 250
else: #units>200:
    total_bill=(100*5)+(units-200)*10 # rs 5 for next 100 units & charge rs 10 each units beyond 200
print(f"Amount to pay is {total_bill}")
#
# 250
# 100=0
# 100*5=500 +
# 50*10=500 (units-200) *50


#5) Write a program to display the last digit of a number, also find out that last digit is divisble by 3 or not

number=int(324)

last_digit=number%10
print(last_digit)
if last_digit%3==0:
    print("Your last digit number is divisible by 3")
else:
    print("not divisible by 3")


### Practice Set2
#6 ) write a program to accept a percentage from the user and display the grade according to the following criteria

percentage=100

if percentage>=101:
    print("Please verify your percentage again")
    exit()

if percentage>=90:
    print("Excellent! You have obtained grade A")

elif percentage>80 and percentage<=90:
    print("Very Good! You have obtained grade B")

elif percentage>=60 and percentage<=80:
    print("Good! You have obtained Grade C")

else:
    print("Oh no! you have obtained grade D")


#7 ) write a program to accept the cost price of Bike and display the road tax to be paid according to the following criteria
'''
>100000 15%
>50,000 and <=100000 10%
<=50,0000  5%
'''
cost= float(51243.23)
tax_amount=0
if cost>100000:
    tax_amount=(15/100)*cost
elif cost>50000 and cost<=100000:
    tax_amount=(10/100)*cost
else:
    tax_amount=(5/100)*cost
print(f"the road tax cost of you bike is rs {tax_amount:.0f} ")


#8) Write a program to check if the years is leap or not?
year=int (2010)
'''
# A year is a leap year if:
# 1. It is divisible by 4 and not divisible by 100, or
# 2. It is divisible by 400
'''

print("leap year") if (year%4==0 and year%100!=0) or year%400==0 else print("Not Leap year")



#9) Write a program to accept a number from 1 to 7 and display the name of the day like 1 or sunday 2 for monday & so on

users=int (7)

if users==1:
    print("Sunday")
elif users==2:
    print("Monday")
elif users==3:
    print("Tuesday")
elif users==4:
    print("Wednesday")
elif users==5:
    print("Thursday")
elif users==6:
    print("Friday")
elif users==7:
    print("Saturday")
else:
    print("you choose wrong input")

#10) Write a program to accept a number from 1 to 12, and display the name of month and days in that month like 1 for January and number of days 31 and so on,

users=int(3)
if users==1:
    print("Jan")
elif users==2:
    print("Feb")
elif users==3:
    print("Mar")
elif users==4:
    print("April")
elif users==5:
    print("May")
elif users==6:
    print("June")
elif users==7:
    print("July")
elif users==8:
    print("Aug")
elif users==8:
    print("Sept")
elif users==8:
    print("Oct")
elif users==8:
    print("Nov")
elif users==8:
    print("Dec")
else:
    print("wrong input")


# check the output

if True:
    print(101)
else:
    print(202)


##11) Accept any city from the user and display the monument of that city

city="pokhara"

print ("Pasupatinath") if city=="kathmandu" else print("Phewa Lake") if city=="pokhara" else print ("Sauraha National Park") if city=="chitwan" else print("input is wrong")


#PracticeTest3

#12) Write a program to check whether the entered number is 3digit number or not

number=str(324)

if len(number)==3:
    print(" it's 3 digit number")
else:
    print("not 3 digits")

#13) Write a program to find the lowest number out of two numbers expected from the user.

first_number=int(20)
second_number=int (30)

if first_number> second_number:
    print("second is lowest number")
else:
    print("first is the lowest number")


#14) Write a program to find the lowest number out of two numbers expected from the user.

first_number=int(50)
second_number=int(22)

if first_number> second_number:
    print(" first is the highest number")
else:
    print("second is the highest number")

#15) Write a program whether a number is positive or negative.

first_number=int (21)
if first_number>0:
    print("it's positive number")
else:
    print("it's negative number")


#16) Write a program to check whether the number is even or odd

number=int (50)
print("even") if number%2==0 else print("odd")

#17) Write a program to check whether the number is divisible by 2 and 3 both

number=int(20)

print("number is divisible  by 2 & 3") if number%2==0 and number%3==0 else print("not divisible")



#18) Write a program to find the largest number out of three numbers expected from the user.

num1=int (5)
num2=int (8)
num3=int (7)
if num1>num2 and num1>num3:
    print("num1 is the largest")
elif num2>num1 and num2>num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")



###Practice Test 6
#19)Accepts the three number from the user and display the second largest number

# num1=int(input("first number")) #8
# num2=int(input("second number")) #7
# num3=int(input("third number")) #1

num1=7
num2=11
num3=4
# if(num1>num2 and num1<num3) or (num1<num2 and num1>num3):
#     print("num1 is the second highest")
# if(num2>num1 and num2<num3) or( num2<num1 and num2>num3):
#     print("num2 is the second highest")
# if(num3>num2 and num3<num1) or (num3<num2 and num3>num1):
#     print("num3 is the second highest")

if(num1>=num2 and num1<=num3) or (num1<=num2 and num1>=num3):
    second_highest=num1
    print("num1")
elif (num2>=num1 and num2<=num3) or (num2<=num1 and num2>=num3):
    second_highest=num2
    print("num2")
else:
    second_highest=num3
    print("num3")
print("the second highest number is", second_highest)


#20) Accept the three sides of triangle and check whether the triangle is possible or not
x=10
y=10
z=10

if (x+y)>z and (y+z)>x and (x+z)>y:
    print("it's a triangle")
else:
    print("Not triangle")

#23
i=3
j=5
k=7
if i>j:#2>4
    if j>k:#4>5
        i=j #6
    else:
        j=k #5
else:
    if j>k:
        j=i #2
    else:
        i=k #5
print(i,j,k)

#5, 5, 7
#9,-5,-9
#8, 12, 12
#13, 13, 13
#5, 5, 17
#17, 25, 17


i=-2
j=-5

if i>j:
    print(True)
else:
    print(False)


#24)  Accept the units from the user and calculate the bill according to following

'''
First units 100 Free
Next 200 units      rs 2per day
Above 300 units   rs 5 per day
'''
units=int (500)

bill=0

#if the units is equal to 100 or less than 100
if units<=100:
    bill=0  # First 100 units are free
# For the next 200 units, Rs 2 per unit
elif units<=300:
    bill=(units-100)*2
else:
    bill=(200*2)+(units-300)*5 # Rs 2 for the next 200 units, Rs 5 for units above 300
print("your total bill is rs", bill)

#25) Accept the number from the days from the user and calculate the charge for library according to the following

'''
Till five days : rs 2 per day
Six to ten days: rs 3 per day
11 to 15 days :rs 4 per day
After 15 days: rs 5 per day
'''
days=16
charge=0
if days<=5:
    charge=days* 2 # Rs 2 per day for the first 5 days
elif days>=6 and days<=10:
    charge=(2*5)+(days-5)*3 # Rs 2 for first 5 days, Rs 3 for days 6-10
elif days>=11 and days<=15:
    charge=(2*5)+ (5*3) +(days-10) *4 # Rs 2 for first 5 days, Rs 3 for days 6-10, Rs 4 for days 11-15
else:
    charge=(2*5) +(3*5)+ (4*5) +(days-15)*5   # Rs 2 for first 5, Rs 3 for next 5, Rs 4 for next 5, Rs 5 after 15

print("your total charge is ", charge)


#26 Accept the kilometers covered and calculate the bill according to the following criteria

'''
first 10 km  rs 11/km
Next 90km  rs10/km
after that  rs 9/km
'''

km=int(100)
bill=0
if km<=10:
    bill=km*11
elif km>=90:
    bill=(10*11)+(km-10)*10
else:
    bill=(10*11) +(km-10)*10 +(km-90)*9

print(f"Your total covered km is{km} and ", bill)


#27) Accept the marks of english, math and science, social studies subject and display the stream allocated according the following

'''
All subjects more than 80 marks  --- Science Stream
English>80 and Math, science>50 --- Commerce Stream
English>80 and social studies> 80 --- Humanities Stream
'''
english=92
science=82
math=93
social=72

if english>80 and science>80 and math>80 and social>80:
    stream="Science"
elif english>80 and math>50 and science>50:
    stream="Commerce"
elif english>80 and social>80:
    stream ="Humanities"
else:
    stream="No eligible stream"
print("you are eligible for " + stream +" stream")




###Practice Set 5

#28) Accept the following from the user and calculate the percentage of class attended

'''
Total number of working days
total number of days of absent

if the percentage is less than 75, student will not able to sit in the exam
'''
working_days=120
absent_days=70

class_attend=int(working_days-absent_days)
percentage=class_attend/working_days *100

if percentage<75:
    print(f"your class attended is {percentage:.0f}%,  You can't sit in the exam")
else:
    print(f"your class attended is {percentage:.0f}%,  Good luck for the exam")


#29) Accept the percentage from the user and display the grade according to the following criteria

'''
Below 25 --D grade
25 to 45 --C Grade
45 to 50 -- B Grade
50 to 60-- B+ Grade
60 to 80--- A grade
80-- above --- A +grade
'''

percentage=45

if percentage<25:
    grade="D"
elif percentage<=45:
    grade="C"
elif percentage<=50:
    grade="B"
elif percentage<=60:
    grade="B+"
elif percentage<=80:
    grade="A"
elif percentage>80 and percentage<=100:
    grade="A+"
else:
   grade="wrong percentage"
print("Your grade is "+ grade)


#30) A company decide to give bonus to their employee according to this criteria

'''
More than 10 years --10%
>=6 and <=10 --- 8%
less than 6 years ---5%

ask the users for their salary and working period to findout the bonus
'''
salary=500
period=18

if period>10:
    salary+=10/100*salary
elif period>=6 and period<=10:
    salary+=8/10*salary
elif period<6:
    salary+=5/10*salary
print("your total salary with the bonus is ", salary)


#31) Accept the marked price from the user and calculate the Net amount as (Marked Price-Discount) to pay according to the following

'''
>100000 20%
>7000 and <=10000   15%
<=7000 10% 
'''

mp=int(120000)
discount=0
if mp>100000:
    discount=20/100*mp
    print(discount)
elif mp>7000 and mp<=1000:
    discount=15/100*mp
elif mp<=7000:
    discount=10/100*mp
net_amount=mp-discount
print(f"the net amount is {net_amount}")


#32) Accepts three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle

'''
equilateral triangle-- all sides are equal
scalene -- three unequal sides
isosceles-- at least two sides are equal
'''

x=10
y=10
z=10

if x==y==z:
    print("Equilateral triangle")
elif x==y!=z or y==z!=x or z==x!=y:
    print("Isosceles Triangle")
else:
    print("Scalene triangle")


#33 write a program to accept two numbers and mathematical operation and perform calculations

'''
num1=7
num2=5
op=+
'''
num1=int(3)
num2=int(5)
opr="%"

if opr=="+":
    result=num1+num2
elif opr=="-":
    result=num1-num2
elif opr=="*":
    result=num1*num2
elif opr=="/":
    result=num1/num2
elif opr=="**":
    result=num1**num2
elif opr=="//":
    result=num1//num2
elif opr=="%":
    result=num1%num2
else:
    result="you choose wrong opr"

print(f"the result is {result}")

###34) Accept the age, sex (M,F), number of days and display the wages according to the criteria

'''
>=18 and <30    male= rs 700, female=rs 750
>=30 and <=40    male rs 800, female =rs 850
'''

age=18
sex="m"
days=20
wages=0
if age>=18 and age<30:

    if sex=="m":
        wages=700*days
    elif sex=="f":
        wages=750*days
    else:
        print("choose between m and f")
elif age>=30 and age<=40:
    if sex=="m":
        wages=800*days
    elif sex=="f":
        wages=850*days
    else:
        print("choose between  m and f")
else:
    print("not allow to work as an labour")

if wages > 0:
    print("The total wage is:", wages)

#next method
wages=0
if age>=18 and age<30 and sex.lower()=="m":
    wages=700*days

elif age>=18 and age<30 and sex.lower()=="f":
    wages=750*days

elif age>=30 and age<=40 and sex.lower()=="m":
    wages=800*days

elif  age>=30 and age<=40 and sex.lower()=="f":
    wages=850*days

print("total wages", wages)


#36) Accept the age of 4 people and display the youngest one

p1=6
p2=5
p3=3
p4=10

if p1<p2 and p1<p3 and p1<p4:
    print("p1 is youngest", p1)
elif p2<p1 and p2<p3 and p2<p4:
    print("p2 is the youngest", p2)
elif p3<p1 and p3<p2 and p3<p4:
    print("p3 is the youngest", p3)
else:
    print("p4 is the youngest", p4)


#37) Accept the age of 4 people and display the oldest one

p1=6
p2=5
p3=3
p4=10

if p1>p2 and p1>p3 and p1>p4:
    print("p1 is oldest", p1)
elif p2>p1 and p2>p3 and p2>p4:
    print("p2 is the youngest", p2)
elif p3>p1 and p3>p2 and p3>p4:
    print("p3 is the youngest", p3)
else:
    print("p4 is the oldest", p4)


#38) Move tickets are price based on age: $12 for adults (18 and over), $8 for children.
#everyone gets a $2 discount on Wednesday

age=15
days="wednesday"

price=12 if age>=18 else 8 #shorthand

###



if days=="wednesday":
    price-=2
print("Ticket price is $", price)



is_wednesday=True
if age<18:
    price=8
    if is_wednesday:
        price=price-2
else:
    price=12
    if is_wednesday:
        price=price-2
print("total price", price)



#39) Coffee customization
#customize a coffee order: "Small", or "Large", with an option for an "Extra shot" of expresso

size="Small"
extra_shot=True

if extra_shot:
    coffee=size + "coffee with extra shot"
else:
    coffee=size+"coffee"

print("Order:",coffee )


#Revise leap year

year=2000

if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("Not Leap year")


#40)Password Strength Checker

password="dahjghyffgd5767878743eytiu"

length=len(password)

if length>=12:
    print("your password is very strong")
elif length>=8:
    print("your password security is moderate")
else:
    print("password is weak")


#41) pet food recommendation
species="Dog"
age=2

if species.lower() =="dog" and age<=2:
    print(f"Feed!, PuppyFood as it's species {species}")
elif species.lower()=="cat" and age<5:
    print(f"feed,  Senior Cat food as it is species,{species}")
else:
    print("please choose between cats and dog as species")

