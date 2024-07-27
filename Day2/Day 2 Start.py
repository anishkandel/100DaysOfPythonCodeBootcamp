# #Data Types
# #String
# #int
# #Float
# #boolean

# #character surrounded by quotes called a string


# #****************Python Primitive DataTypes****************
print(len("Hello"))

print("Hello"[0])
# #Subscripting means pulling out a particular element from a string
print("Hello"[4])

print ("123" + "345")
# # it is basically concatenating the strings


# #Integar
print(123 + 456)

# #Large Integars
print(123_456_789) 
# #when we have to write large numbers we can use underscore to make it more readable like we use commas in english.


# #Float DataTyoe
# 1.34546



# #Boolean

# #it only has two possible values True or False (1 or 0))

# #1=True and 0=False



# #********* Type Error, Type Checking and Type Conversion******************
# # len(273723)
# #len function is does not work with integers

num_char=len(input("what is your name?")) # we take the integar data type put it inside the parenthesis of a str function which takes a obj in between the paranthesis and coverts into a string

new_num_char=str(num_char) # we store the value in new variable
print("Your name has "  + new_num_char + " characters.")

# #So we only concatenate strings (str)  with strings but not strings with integars (int)

# #we can use type() function to check the data type of a variable
print(type(num_char))
type_of_variable=type(num_char)
print(type_of_variable)

# #type conversion or type casting 
new_num_char=str(num_char)

a= str(12233)
print(type(a))

b= float(366355)
print(type(a))


print(80+ float("20.5"))

# # here we will get 100.5 as the output, we are conversion or casting the string data type to float and the adding it to the integer data type 80

print(str(10) + str(100))

# #in Summary, we can use type function to investigate the data type, we are working with and we can use functions like string, int, or float to convert that data type




# # Excerise 1

two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
print(type(two_digit_number))  # we get int type for eg 45

first_digit=int(two_digit_number[0]) # we stored first value on first_digit variable
second_digit=int(two_digit_number[1]) # we stored 2nd value of input in second_digit variable

two_digit_number= first_digit + second_digit # we converted the string data type to integer data type and then stored the sum in sum_of_two_digit variable

print(two_digit_number)




#**************************Mathematical Operation in Python********************************************


#PEMDASLR rule

#parenthesis ()
#exponenets **
#multiplication * #division /
#substraction - #addition +


#add
print(3+5)
print(3_5_6+2_1_2)

# #multiplication
print(3*2)

# ##division

print(10/5)

# #sub

print(4-1)


print(3*3+3/3-3)
print(3*3/(3+3)-3) # higher priority will be given to multiply, (), /
print(3*(3+3)/3-3)
print(3/3*3+3-3)
print(5-2*3/3+3)




#### ******************BMI CALCULATOR*********************

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height_as_float=float(height)
weight_as_int=int(weight)

#using the exponenet operator **
bmi=weight_as_int//(height_as_float**2)

# using the multiplication and PEMDAS
bmi=weight_as_int/(height_as_float*height_as_float)

print(type(bmi))
bmi_as_int=int(bmi)
print(bmi_as_int)
print ("Your BMI is " + str (bmi_as_int))



#******************Number Manipulation and F Strings in Python******************************
print(int(7/3))
#In python to round off the number we use round function
print(round(7/3, 5)) # here we are rounding off the number to 5 decimal places
print(round(2.8776473, 3)) #here we are rounding off the number to 3 decimal places and our output is 2.878

#another way to round off the number is using floor division //
print(7//3)
print(type(7//3)) # here we get the integer data type
print(type(7/3)) # here we get the float data type


total_result=6/3
total_result/=2

print(total_result)


score=2


#use  scores a point
score*=1
score+=5
score-=2
score/=2
print(score)

print("Your total score is " + str(score))


#******F-Strings**********
#F-string is used to combine different data types in a single string and its make the code more readable
score=int(input("What is your integar score? \n "))
height= float(input("what is your height? \n"))
isWinning=bool(input("Are you wiining?, answer on True or False \n"))

print(f"Your score is {score} and your height is {height} and you are winning is {isWinning} ")

#see F-strings makes the code more readable and we can use it in python


###*** Excerise 2*******************

# age = input("What is your age?")
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# #first we have find out total weeks in 90 years

# weeks_in_year=52
# print(weeks_in_year)

# total_weeks=90*weeks_in_year
# print(total_weeks)

# user_age=int(age)

# user_lived_weeks=user_age* weeks_in_year
# # print(user_lived_weeks)

# week_left=(total_weeks-user_lived_weeks)

# print(f"You have {week_left} weeks left.")

age = input("What is your age?")
years= 90-int(age)
weeks= years * 52

print(f"You have {weeks} weeks left.")
