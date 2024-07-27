#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

#let's ask for the bill
bill=float(input("What was the total bill?" + "\n$"))

#let's decide the tip percentage to add the bill
tip_percentage= float(input("how much tip percentage would you like to give? 10, 12, 15 \n %"))

#let ask the number of people
people=int(input("How many people are going to split the bill? \n "))

# print(type(tip_percentage))

# print(type(total_bill))
#let's know the tip amount in $
tip=(bill* (tip_percentage/100))
print(type(tip))

#let's add tip amount in the bill to get total bill to pay
total_bill= bill + tip
print(total_bill)

#let's divide the tota bill by people to find each bill to pay
each_bill=(total_bill/people)


#let's round of with 2 decimal of each final amount to pay

#final_amount_per_person= round(each_bill, 2)

#here we use format function to round the number to 2 decimal places

final_amount_per_person="{:.2f}".format(each_bill)


print(type(each_bill))


# print(tip)

#let's print the final output
print(f"Each person should pay ${final_amount_per_person}")
##float also can't concate with string

