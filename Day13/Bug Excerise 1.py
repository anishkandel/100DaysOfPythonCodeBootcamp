#bug 
def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."



#solved
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
ask_number = int(input("Tell me a number"))
print(odd_or_even(ask_number))