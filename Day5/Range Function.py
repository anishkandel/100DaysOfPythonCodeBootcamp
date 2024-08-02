# even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
# 
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# 
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
# 
# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.
# 

target = int(input("Enter a number between 0 and 1000")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️


# Write your code here 👇

sum=0
for number in range(2, (target+1), 2):
  sum+=number
print(sum)  



#Another way
output=0

for n in range (1, target+1):
  if n%2==0:
   output+=n
  
print(output)