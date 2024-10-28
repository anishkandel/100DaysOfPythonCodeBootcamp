#Q1: write a python program to sum all items in a list
from operator import indexOf

a=[1,2,3,4,5,6,7]
sum_number=0
for x in a:
  sum_number+=x
print(sum_number)

# using function

def sum_list(items):
    sum_numbers=0
    for y in items:
        sum_numbers*=y
    return sum_numbers

print(sum_list([1,2,3,4,5,6]))

#Q2) Write a Python program to multiply all the items in a list.

def multiply_list(items):
    # when we have multiply, we have to initialize with 1
    result=1
    for z in items:  #This line starts a loop that will iterate over each element in the items list, one at a time.
      result*=z
    # Return the final product of the numbers
    return result #his line returns the final value of the tot variable after the loop has finished. This is the product of all the numbers in the items list.
print(multiply_list([5,6])) #This line calls the multiply_list() function and passes in the list [5, 6]. The resulting product is then printed to the console using the print function.

#3. Write a Python program to get the largest number from a list.
def large_num(items): # defines a function called large_num that takes a single argument list.
    max_num=items[0] ## Initialize a variable 'max_num' with the first element of the input list as the initial maximum
    for num in items: #200
        if num>max_num:  # Check if the current element 'num' is greater than the current maximum 'max_num'
            max_num=num
    return max_num
print(large_num([200,12,43,56,324,764,42]))


#4. Write a Python program to get the smallest number from a list.

def small_num(items):
    min_num=items[0] #1
    for num in items:
        if num<min_num:
            min_num=num
    return min_num
print(small_num([5,6,7,3,30,400]))

# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_num(items):#['abc', 'xyz', 'aba', '1221']
    result=0
    for word in items: #'abc'
# Check if the word has a length greater than 1 and its first and last characters are the same
        if len(word)>1 and word[0]==word[-1]:
            result+=1
    return result
print(count_num(['abc', 'xyz', 'aba', 'cdc', '1221']))


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def last(n):
    ''' we defined a func called 'last' that takes a single argument n.
    This function returns the last element of 'n' '''
    return n[-1] #
print(last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
def sorted_list_tuples(tuples):
    ''' we defined a func called 'sorted_list_tuples' that takes a single argument tuple
    this function sort the input lists of tuple based on the last each element of the tuple
    using the sorted function and the key parameter
    the key parameter specifies a function to be called on each element of the list to determine
    the sort order. In this case, the last func is used as the key function,
    so the sorting is based on the last element of each tuple.
    '''
    sorted_result=sorted(tuples, key=last) #key will sort every last element of tuple
    return sorted_result

print(sorted_list_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))




#7. Write a Python program to remove duplicates from a list.

# empty list to store duplicate items
def duplicates(items):
    not_dup_list=[]

    for x in items:
       if x not in not_dup_list: # it iterates every item and check if it already in the new list or not
           not_dup_list.append(x)
    return not_dup_list

print(duplicates([1,2,3,3,2,5,6,3]))


# empty set to store duplicate items
def duplicates(items):
    not_dup_list=set() # set allows ordered and no duplci

    for x in items:
       if x not in not_dup_list: # it iterates every item and check if it already in the new list or not
           not_dup_list.add(x)  # for set we use add instead to append in list
    return not_dup_list

print(duplicates([1,2,3,3,2,5,6,3]))

# Create an empty set to store duplicate items and an empty list for unique items

def duplicates(items):
    dup_items = set() # sets are ordered and not allow duplicates
    unique_items = []
    for b in items:
        # Check if the current element 'x' is not already in the set 'dup_items' (it's a duplicate check)
        if b not in dup_items:
            unique_items.append(b)
            # Add 'x' to the 'dup_items' set to mark it as a seen item
            dup_items.add(b)
    print(dup_items)
    return unique_items

sample_list = [1,1,2,2,3,6,7,8,5]
result= duplicates(sample_list)
print(result)


#8 Write a Python program to check if a list is empty or not.

def empty(items): #[1,2,3,4,5]
   if len(items)==0:
       return "list is empty"
   else:
       return "list is not empty"

print(empty([]))

# using not keyword

l=[] # This line creates an empty list called 'l'. the boolean value is false with empty value
if not l: #code checks if the list 'l' is empty using the not keyword, which checks if a value is False. If 'l' is empty, the condition is true, and the code block inside the if statement will execute.
    print("list is empty")

#9. Write a Python program to clone or copy a list.

a=[1,2,3,4,5,6]
b=a.copy()
print(b)

#10. Write a Python program to find the list of words that are longer than n from a given list of words.

n=["abc", "sm","bc","def" "a"]
b=[]
for i in n:
    if len(i)>2:
        b.append(i)
print(b)

def user(word):
    new_word=[]
    txt=word.split(" ") # as we are passing argument as a sentence, we have to split it into separate strings
    for x in txt:
        if len(x)>3:
            new_word.append(x)
    return new_word
print(user("the quick and clever fox jumps out of the wall"))

## if we want take both input word as well as number

def user(number, sentence):
    new_word=[]
    txt=sentence.split(" ")
    for i in txt:
        if len(i)>number:
           new_word.append(i)
    return new_word
print(user(2,"the crazy and lazy fox are so stupid"))


# Define a function called 'long_words' that takes an integer 'n' and a string 'str' as input
def long_words(n, str):
    # Create an empty list 'word_len' to store words longer than 'n' characters
    word_len = []

    # Split the input string 'str' into a list of words using space as the delimiter
    txt = str.split(" ")

    # Iterate through each word 'x' in the list of words 'txt'
    for x in txt:
        # Check if the length of the current word 'x' is greater than 'n'
        if len(x) > n:
            # If the word is longer than 'n' characters, add it to the 'word_len' list
            word_len.append(x)

    # Return the list of words longer than 'n' characters
    return word_len

# Call the 'long_words' function with an 'n' value of 3 and a string as input, and print the result
print(long_words(3, "The quick brown fox jumps over the lazy dog"))



#11. Write a Python function that takes two lists and returns True if they have at least one common member.
def myFunc(list1, list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
    return result


print(myFunc(["small","big","large","medium","verybig"],["small","notsmall","big"]))
print(myFunc([1,2,3,4,5],[6,7,8,9]))



#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new_color=[]
for (i,x) in enumerate(color): #i=index , x=value
    print(i,x)
    if i not in (0,4,5):
        new_color.append(x)
color=new_color
print(color)
#list comprehension
'''
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]  -> Creates a new list using a list comprehension. The list comprehension loops over each element (i, x) in color and includes only those elements where i is not in (0, 4, 5).

enumerate(color) returns a list of tuples containing the index and value of each element in color.

(i, x) unpacks each tuple into two variables, i and x.

if i not in (0, 4, 5) checks if the index of the current element is not equal to 0, 4 or 5.

[x for ...] creates a new list containing only the values of the elements that meet the condition specified in the if statement.

After this code runs, the list color will only contain the elements that have an index of 1, 2, or 3. So, the colors 'Green', 'White', and 'Black' will be included, and 'Red', 'Pink', and 'Yellow' will be removed.


'''

#list comprehension
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
print(color)



#example of basic list comprehension
color=['Red', 'Gre', 'White', 'Bla', 'Pink', 'Yellow']
new_color=[ x for x in color if len(x)>3]
print(new_color)


#13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
new_list=[]
for row in range(3):
    print(row)
    row_list=[]
    for col in range(4):
        col_list=[]
        for col2 in range(6):
            col_list.append("1, 2,3")
        row_list.append(col_list)
    new_list.append(row_list)

print(new_list)

# array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]

#14 Write a Python program to print the numbers of a specified list after removing even numbers from it.

def program(items):
    even_num=[]
    new_items=[]
    for i in items:
        if i%2==0:
            even_num.append(i)

        if i not in even_num:
            new_items.append(i)

    print("the even num from the list is", even_num)
    print("the new items without the even num is", new_items)
    return even_num, new_items


print(program([1,2,3,4,5,6,7,8,9,22, 29,43,42,35,34,78,89]))

##short hand
num=[1,2,3,4,5,6,7,8,9,22, 29,43,42,35,34,78,89]

not_even=[x for x in num if x%2!=0 ]
print ("items without even number of the list", not_even)

#15 Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

shuffle(color)

print(color)

#16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).




def square_values():
    square=[] #sqaure=list()
    for i in range(1, 31):
         square.append(i**2)
    print("sqaure values of first five elements are", square[:5])
    print("sqaure values of last 5 elements are", square[25:])



square_values()



#17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False


# 6n ± 1 where, n = natural number >3



def is_prime(n):
       # Check if 'n' is equal to or less than 1; if so, it's not prime
       if n <=1:
           return False
       # Check if 'n' is equal to 2; if so, it's prime
       for i in range(2, int(n**0.5) +1):
             print(i)
             if n%i==0:
                return False
       return True


def all_prime(numbers):
           for num in numbers:
               if not is_prime(num):
                   return False
           return True


print(is_prime(2))
print(all_prime([0, 3, 4, 7, 9]))


#18. Write a  Python program to generate all permutations of a list in Python.
'''permutation relates to the act of arranging all the members of a set into some sequence or order, 
or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. T'''

import itertools

#user itertools.permutation to generate all permutations of the list [1, 2, 3] and covert the result to a list
#The "List" will produce all possible orderings of the elements in the list

print(list(itertools.permutations([1,2,3])))

#19. Write a Python program to calculate the difference between the two lists.


list3=[]

def num(n1, n2):
    for i in n1:
        if i not in n2:
            list3.append(i)
    for i in n2:
        if i not in n1:
            list3.append(i)

num( [1, 3, 5, 7, 9],[1, 2, 4, 6, 7, 8])
print(list3)


def  num(n1, n2):
   list1=list(set(n1)- set(n2))
   list2= list(set(n2)-set(n1))
   total_diff=list2+list1
   print (total_diff)

num ([1,2,45,6,78],[234,5,67,2,4,1])


#20. Write a Python program to convert a list of characters into a string.

list1=['a', 'b', 'c','d']
str1="".join(list1)

print(str1)


#21. Write a Python program to find the index of an item in a specified list.

items1=["apple", "orange", "grapes", 55, "melon"]
for i in items1:

  print("the index of ", i,"is", items1.index(i))

#22 Write a Python program to append a list to the second list.

fList=[1,2,3,4,5]
sList=["apple", "banana", "cherry","grapes", "melon"]

for i in sList:
    fList.append(i)
print(fList)

#23. Write a Python program to select an item randomly from a list.
import random
list1=['a', 12, "apple", 2, 4]

random_item=random.choice(list1)
print(random_item)

#24  Write a Python program to check whether two lists are circularly identical.

def listdiff(n1, n2):
        if n1==n2:
            print("Lists are idententical")
        else:
            print ("Not Identical")

listdiff([1,2,3,4,5,6],[2,3,4,5,9,0])

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]


print("Compare list1 and list2")
# Check if the string representation of list2 is present in the string representation of list1 repeated twice
# The result will be True if list2 is a subsequence of list1 repeated twice, otherwise False
from typing import final

print(''.join(map(str, list2)) in ''.join(map(str, list1*2)))

print("Compare list1 and list3")

print(''.join(map(str, list3)) in ''.join(map(str, list1*2)))



#25 Write a Python program to find the second smallest number in a list.

def second_smallest_number(n1):
  #check is the number is less than 2
  if len(n1)<2:
      return
  #check if there are only two elements in the list and they are same
  if len(n1)==2 & n1[0]==n1[1]:
      return
  #creating a empty set to store duplicate items and unique items to store unique items
  dup_items=set()
  unique_items=[]
 #iterate through the elements in the number lists
  for x in n1:
      #check if x is not in dup items, if not, add it unique items and dup items
     if x not in dup_items:
         unique_items.append(x)
         dup_items.add(x)
     #sort the unique item list in ascending order
     unique_items.sort()
     print(unique_items)
    # Return the second smallest item from the sorted 'uniq_items' list, which is at index 1
  return(unique_items[1])

print(second_smallest_number([12,4,6,98,34,56,2,45,3,6]))


#26 Write a Python program to find the second smallest number in a list.



def second_highest_num(n1):
# first ma list ko length 2 vanda kam nahos
  if len(n1)<2:
      return
# second highest ko lagi, we need at least three elements in the list and tini haru same hunu vayena
  if len(n1)==2 and n1[0]==n1[1]:
      return

#creating dup_items set to store duplicate value and unique items to store unique value
  dup_items=set()
  unique_items=[]

  for x in n1:
      #check if n1 is in duplicate items, if not add to unique items
      if x not in dup_items:
          unique_items.append(x)
          dup_items.add(x)
          #sort  the unique items in ascending order
      unique_items.sort()
  print("Duplicate items :", dup_items)
  print("unique Items are ", unique_items)

  return unique_items[-2]

print("The second highest number is ", second_highest_num([1,4,3,5,56,78,34,5, 3,79,100,245]))



#26 Write a  Python program to get unique values from a list.

my_list=[1,2,3,5,3,1,6,7,8,9,4]

print("My original list :", my_list)

my_set=set(my_list) # removing duplicates and put it in order

print(my_set)

#Convert the 'my_set' back to a list 'my_new_list' to obtain a list of unique numbers
my_new_list= list(my_set)
print("list of unique numbers" ,my_new_list)

#27  Write a Python program to get the frequency of elements in a list. (collection.counter)

import collections
my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

print("my original list", my_list)

frequency_of_elements=collections.Counter(my_list)

print ("the frequncy of the elements in the my_list :",  frequency_of_elements)



#28) Write a Python function to reverse a list at a specific location.

























rock = ''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
symbol=[rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(symbol[user_choice])


comp_choice=random.randint(0,2)
print("Computer Choose:")
print(symbol[comp_choice] )


if (user_choice==0 and comp_choice==2) or (user_choice==2 and comp_choice==1) or (user_choice==1 and comp_choice==0):
    print("user wins")
elif user_choice==comp_choice:
    print("draw")
else:
    print("computer wins")


#toss game
coin=random.randint(0,1)

if coin==1:
    print("head")
else:
    print("tails")


#who will pay the bill, russian roulette
friends=["anish", "shree","kandel", "dego"]

payer=random.choice(friends)
print(payer)

#OR

bill=random.randint(0,4)
print(friends[bill])


#random.random()
#random.uniform


#
# Generate a Random Float
# Write a program that generates and prints a random floating-point number between 0 and 1 using the random() function.

print(random.random())


# Simulate a Dice Roll
# Use randint() to simulate rolling a six-sided die. The program should print a random integer between 1 and 6.

dice=random.randint(1,6)
print("You get",dice)

# Random Password Generator
# Write a program that generates a random 8-character password using letters, numbers, and special characters. Use random.choice() to pick characters randomly from a predefined set.

letters=["a", "A", "b","c", "D","e","f","g","h","I","J", "k","l", "#","&","%","@",1, 2, 3, 4, 5, 6,7,8,9,0]

password=random.choices(letters, k=8)

final_password = ''.join(str(char) for char in password)

print("Your Password is", final_password)

# Pick a Random Element
# Create a list of 10 colors. Write a program that selects a random color from the list using random.choice().

colors=["blue","red","brinjal","yellow","green","purple","white"]
print(random.choice(colors))

#
# Simulate a Coin Flip
# Write a program that simulates flipping a coin 100 times and counts how many times it lands on heads or tails. Use random.choice() with a list of ["Heads", "Tails"].


side=["Head", "Tails"]
head_times=0
tail_times=0
for i in range(100):
    flip=random.choice(side)
    if flip=="Head":
        head_times+=1
    else:
        tail_times+=1
print(head_times, tail_times)



#Shuffle a List
#Write a program that shuffles a deck of cards (or any list of items) using random.shuffle(). Print the list before and after shuffling.
cards=[1,2, 3,4,5,6,7,8,9,10,11,12,13]
print(cards)
random.shuffle(cards)
print(cards)

#
# Random Number in a Range
# Write a program that generates a random integer between two user-specified numbers using randrange(). Ensure the user inputs the start and end values.

start=int(input("enter the start value"))
end=int(input("enter the end value"))
random_number=random.randrange(start, end+1)

print(f"The random value between {start} and {end} is: {random_number}")


#
# Random Lottery Numbers
# Create a program that generates six random lottery numbers between 1 and 49 using random.sample(). Ensure no number repeats.

start=1
end=49
# Generate six unique random lottery numbers
#The range(start, end + 1) generates numbers from 1 to 49 inclusive.
lottery_numbers=random.sample(range(start, end+1), 6)

print("your lottery numbers are ", lottery_numbers)


#
