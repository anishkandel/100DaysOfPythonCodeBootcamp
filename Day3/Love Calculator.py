print("The Love Calculator is calculating your score...")
name1=input("What is your name?")
name2=input("What is your lover name?")


combined_names=name1+name2

lower_name=combined_names.lower()

t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")

first_score= t+r+u+e

l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")

second_score=l+o+v+e

#adding two strings and chaning it into integar, becuase we have to use comparison operators after this
final_score=int(str(first_score)+ str(second_score))


#less than 10 or greater than 90
# the message should be:
# 
# "Your score is *x*, you go together like coke and mentos."

if (final_score<10) or (final_score>90):
    print(f"Your score is {final_score}, you go together like coke and mentos.")
    
#For Love Scores between 40 and 50, the message should be:
elif (final_score>=40) and (final_score<=50):
    print(f"Your score is {final_score}, you are alright together.")

#Otherwise, the message will just be their score. e.g.:
    
else:
    print(f"Your score is {final_score}.")


    




