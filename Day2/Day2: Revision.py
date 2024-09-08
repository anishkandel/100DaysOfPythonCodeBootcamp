# Day2, dATA TYPES, nUMBERS, oPERATIONS, TYPE CONVERSION, f-STRINGS ETC

len("Hello")
'''
 variables can store data of different types such as 
text type: String(str)
Numeric Type: integar(int), float, complex
Sequence type:list, tuple, range
mapping type:dictionary(dict)
Set types: Set, frozenset
Boolen types: bool
Binary types: butes, bytearray, memoryview
None type: NoneType 

#these are the different types of data can do different things.

We can get the data type of any object by using the type() function.



#Setting the Data type
data type is set when assign a value to a variable

#Example 1: Type() function
x, y, z, a, b, c, d, e, f= "hero", 5, 10.5, 1+0j, True,[1, 2,3],{"fruits":"apple","vegies":"tomato"}, {"mango","cherry"}, (1, 2, 3)  #SIgn multiple value into multiple variables in a line
print (type(x), type(y), type(z), type(a), type(b), type(c), type(d), type(e), type(f)) #multiple output in a line

x="hello universe" #str
x=20 #int
x=20.5 #float
x=1j #complex
x=["orange", "mango"] # list
x={"name":"Dego", "age":25} #dict
x={"mango", "orange", "apple"} #set
x=("mango", "apple", "cherry") # tuple
x= fonzenset({"orange", "mango"}) #frozenset
x=range(5) #range
x= True or False #boolen #bool
x= b"Hello" #bytes
x=bytearray(50) #bytearray
x=memoryview(bytes(50)) # memoryview
x=None NoneType


#python Numbers
- Integar (int)
- Float
- Complex

Integar
int is a whole number, positive or negative without decimals, of unlimited length

x=1
y=271643723642376473643
z=-45

Float or Floating Point Number
it is a number, psotive or negative, containing one or more decimals

x=1.0, y=1.10, z=-83.565 


Complex Numbers
-written with a "j" as the imaginary part
z=1+2j, y=6j, z=-7j


Type conversion - Casting
 # there may be times, when we have to sepcify a type of value to a varibale,
 it can be done with casting

process of converting one data type to another
useful, when we are working with data of mixed types(like strings, integars, or float) perform
operations that require them to be of the same type.


# int() - this function converts a value into a integar, it works with
                         #integar literal: keeps the integar as it as.,
                         #float literal: removes the decimal part and converts it to the nearest lower integar (doesn't roundup)
                         #string literal: converts string of digits into a integar, provided the string represents a whole number (no decimal points).

x=int(3.9) #3
y=int('42') #42
z=int(True) #1

Float
x=float(3) #3.0
y=float("42.5") #42.5
z=float("7") #7.0

String
x=str(3) #"3"
y=str(4.5) #"4.5"
z=str(True) # "True"

#Example 2- casting

num_str="10"
num_int= int(num_str)
result =num_int +5
print(result) # 15


x=1 #integar
y=2.8 #float
z=1j #complex

a= float(x) #int to #float
b=int(y) #float to int

c=complex(x) #int to complex

print(a, b, c)
print(type(a), type(b), type(c))


why caSTING?
-DATA CONSISTENCY- when we receives data from the external sources (like files or user input), it's usually in STRING format, casting helps to convert it to the 
correct data type for operations.
-Error prevention
Explicit Control


###### Python Strings ######

surrounded by either single quotation marks ', or double quotation " marks

'hello' is the same as "hello"

 we can display a string literal with 
 print() function 
 print("Hello")



 # Quotes inside quotes

* print ("It's me dego") # It's me dego
* print (' He is known as "PK" ') # He is known as "PK"


## Assign string to a variable
a="Dego"
print(a)


Multiline Strings->


####Strings are Arrays
strings in python are arrays of bytes representing unicode characters.

use square brackets [] to access the characters  by position

a="hello World
print(a[1]) # 


#####Looping through a string.
 We can loop through a string using a for loop.

for a in "Dego":
   print(a) 
#
D
e
g
o


### String length

if we have to find out the length of a string, we can use len()
 a= ("hello, World")
 print(len(a))   #12




#### Check String

 # to check if a certain phrase or characters is present or not in a string, we can use the keyword in and not in

 example1
 check if "dego" is present  in the following variable "name"
name="My name is dego"
print("dego" in name) # true


#check if the substrings doesnot exist ( check if NOT)

#### Use "not in" to check if a phrase or character is missing, 
 Example 2 # check "ted" is not in name variable

name="My name is dego"
print("ted" not in name)   # there is no ted in name # output =True


#check string using if statement

Example 3: print only "dego" is present

name= " My name is dego"
if "dego" in name:
  print(" Yes, "Dego is present")
else:
print("No. "Dego is not present")  


# Check if NOT (using If)

 example4 : print only if "ted" is not present

name= "my name is dego"
if "ted" not in name:
    print("No, 'ted' is not present")
else:
   print("yes, 'ted' is present")

'''

# Some excercise on castings

# 1) Checking multiple substrings in a string
name = "learning Python is fun"
if "Python" and "fun" in name:
    print("both 'Python' and 'fun' are present")

# 2)Using not in with an else statement
txt = "i love coding"
if "boring" not in txt:
    print("'boring' is not present")
else:
    print("'boring' is present")

# 3 Check substring in a loop

fruits = ["apple", "mango", "cherry"]
for fruit in fruits:
    if "a" in fruit:
        print("fruit contains the letter 'a'")
    else:
        print("fruit doesn't contain the letter 'a'")

# 4 check substring at a specific index
txt = "hello world"
if txt[0] == "h":
    print("the string starts with h")


# 5 Using in inside a function

def check_word(sentence, word):  # this is a tes, man
    if word in sentence:
        return f"'{word}' is present"
    else:
        return f" '{word}' is not present"


result = check_word("this is a test", "man")
print(result)

# Other excerise

# exercise 5: check for the vowels in a string,

# Write a program that loops through a string and prints only the vowels

txt = "sjhdhsahcdushddhshgfkdkipweouweerriioesa"
vowels = "aeiou"
for char in txt:
    if char in vowels:
        print(char)

# excerise 5 Count the occurrence of a substring
# write a program that counts how many times the word "love" appears in a give sentence

sentence = "I love to love coding because I love learning python, so I love to be a python developer"
count = 0  # we are intiliazing the count as 0
for word in sentence.split():
    if "love" in word:
        count += 1
print("the word 'love' apears", count, "times")

# Excecise 7 Check for capital letters:
txt = "Hello There"
for char in txt:
    print(char)
    if char.isupper():  # if char will get any uppercase letter
        print(char, "is an uppercase letter")

# excerise 8 print words longer than 4 charcters

sentences = "this is a simple sentences for testing"
for four in sentences.split():
    if len(four) > 4:
        print(four)

# excerise 9 Check if a word ends with a specific letter

words = ['apple', 'orange', 'cherry', 'grape']
for word in words:
    if word.endswith("e"):
        print(word, "ends with 'e'.")

''''
Python Slicing Strings

we can use slicing to extract a part of a string by specifying the start and end indices.

syntax: string[start:end] # end index is not included
syntax: string[start:end: step]

'''
a = "hello world"
print(a[2:5])  # llo # 5 will be included as it is end indices

# The first character has index 0

#####Slice from the start
b = "Hello world"
print(b[:5])  # Hello

###Slice to the end
b = "Hello World"
print(b[2:])  # llo World

####Negative indexing indicates out from the end of the string i.e. -1 is the last char

b = "hello Dego"
print(b[-5:-2])  # De

# Excerise on String Slicing

# 1) extract a substring using slicing
# extract the substring "python" from the string "i am learning python programming"

text = "I am learning python programming"
print(text[14:20])

# 2) Slice from the middle to end
# get the substring from the middle of the string "welcome to the coding world" to the end"

text = "Welcome to the coding world"
print(text[11:])

# 3) Slice using negative index
# extract the last 6 charcaters from the string "data science is amazing"

text = "Data science is amazing"
print(text[-6:])  # mazing

# 4 Extract a portion from the start to a specific position.
# Get the first 10 characters

text = "Learning python is fun and exciting"
print(text[:10])  # Learning P

# 5 Extract a portion with a step
# syntax: string[start:end: step]
# extract every 2nd character from python programming

text = "Python Programming"
print(text[::2])  # : start # : end 2 step

# Modify Strings
# there are some set of built-in methods, that can use on strings modification
'''
1) Uppercase - upper()
a="hello world"
print(a.upper()) # HELLO WORLD

2) Lowercase -Lower()
a="HELLO Wrold"
print(a.lower()) # hello world

3) Remove Whitespace -strip() method removes any whitespace from the begaining or the end
a="hello ,   world!"
print(a.strip())  # "hello World"

4) Replace String- replace()
it replaces a string with another string

a="hello World"
print(a.replace("h", "j")) # jello World


5) Split string- split()
it returns a list where the text between the specified separator becomes the list item.
the split() method splits the strings into substrings, if it finds the instances of the separator

a="hello, world!"
print(a.split(" ,") # ["helo", "World!"]

'''
a = "My name is dego"
print(a.split(","))  # ['My name is dego']
print(a.split())  # ['My','name', 'is', 'dego']

# String concatenation - concatenate , or combine two strings, can use the + operator
a = "hello"
b = "world"
c = a + b
print(c)

# to add space between them
c = a + " " + b
print(c)

'''Format String F -strings

 We cannot combine the strings and numbers using + 
 , if we try to concetanate, we will get an eror

 age=32
 text="My agge is" +age
 print(text) # typeError

 to resove this, we need to either convert that number to srting using str(age)
 or use string formatting techniquies like f-strings or format()

 f-strings prefix the string with f, and any variables and expressions inside {} will be evaluated and inseterd into the string


'''

# Baisc f-string example 1
age = 25
txt = f"My name is Dego, I am {age}"
print(txt)

''''placeholders and modifiers

a placeholder can contain variables, operations, functions and modifiers to format the value
'''
# Example 2
# Adding a placeholder for the price variable

price = 30
txt = f"the price is {price} dollars"
print(txt)

''' Formatting Numbers with Modifiers

'''
# Example4

price = 152
# dispaly the price with 2 decinmal numbers
txt = f"the price is {price:.2f} dollars"
print(txt)

''''Using Python code in placeholders
performing mathematical opeartions or python code inside the {}
placeholders of an f-string
'''
# example5
txt = f"the price is {20 * 5} dollars"
print(txt)

'''Summary of f-strings
1) F-strings allow us to easily combine strings and variable
2) We can add placeholders in the form of {} within the strings
3) Modifiers (like :.2f) allow us to control how the value is formatted
4) We can perform operations or use functions inside the placeholders

'''

'''Escape charcater (\) backslash

it is a bakslash (\) followed by the character, we want to insert
'''
# eg
# txt= "My name is "dego" and my age is 25" # error # syntaxError

# to resolve this error, we have to use the escape character (\)

txt = "My name is \"Dego\" and my age is 25"
print(txt)

'''' Mathematical Operation'''
# PEMDASLR rule

# Paranthesis ()
# Exponents  **
# Multiplication/Division * OR /
# Addition/ Substraction + OR -
# Left to Right


a = (3 * 3 + 3 / 3 - 3)  # 7
print(a)

a = (3 * (3 + 3) / 3 - 3)  # 3
print(a)

''''Booleans-
represents one of two values: True or False.

1) Comparison operators
 print(10>0) #True
 print(10==1) # False
 print(10<5) # False

 2) Using if statements

 a=200
 b=100
 if b>a:
   print("b is  greater than a")
else:
   print("b is not greater than a"


3) bool () fucntion
print(bool("hello")) # true
print(bool(15)) 3 true

print(bool("")) # False
print( bool(0)) # false

Note: empty values, evaluate to false
bool("") # false
bool([]) # FLASE
bool ({}) # false
bool (0)  # false


#### fNCTION RETURNING BOOLEANS

def myFunction():
   return True
print (myFunction()) # true

# Conditional execution

def myFunction():
  return True
if myFunction():
  print("yes")
else:
  print("NO")     


'''


def myFunction():
    return False


if myFunction():
    print("yes")
else:
    print("NO")

'''
Built In function
python also has many built-in functions that return a bool value,
like isinstance() function, which can be used to determine if an object
is of a certain data type.
'''
# check if an object is an integar or not

z = 200
print(isinstance(z, str))  # false
print(isinstance(z, int))  # true

'''Python Operators
are used to perform operations on variables and values

1)Arithmetic Operators
2)Assignment operators
3)Comparsion Operators
4)Logical Operators
5) identity Operators
6) Membership Operators
7)Bitwise Operators
'''

''' Python Arithmetic Operator

+ Addtion
- Subtraction
* Multiplication
/ Division
% Modulus (remainder)
** Exponentiation (to the power)
// Floor Division
'''

''' Python Comparison Operator
== Equal to , x==y
!= Not Equal to , x!=y
> Greater than, x>y
< Less Than, x<y
>=  Greater than or equal to, x>=y
<= Less than or equal to , x<=y


Python Assignment Operator
used to assign values to variables


= , x=5 , x=5
+=, x+=5, x=x+5
-=, x-=5, x=x-5
*=, x*=5, x=x*5
/=, x/=5, x=x/5
%=, x%=5, x=x%5
//=, x//=5, x=x//5
**=, x**=5, x=x**5
&=, x&=5, x=x&5
!=, x!=5, x=x!5
^=, x^=5, x=x^5
>>=, x>>=5, x=x>>5
<<=, x<<=5, x=x<<5
:=, print(x:=3),  x=3 print(x)

'''

#multilne strings
a=
'''Lorem ipsusdk sdbudf
 sdfndkflkidsoifjasdo
'''

print(a)# Lorem ipsusdk sdbudfsdfndkflkidsoifjasdo

# Final Project: tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_amount= (tip/100)*bill
total_bill =bill +tip_amount
final_pay= total_bill/people

print(f"Each person should pay: {final_pay:.2f}")



