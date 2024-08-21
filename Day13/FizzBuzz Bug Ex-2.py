# # Target is the number up to which we count
# def fizz_buzz(target):
def fizz_buzz(target):
    for number in range(1, target+1):
        if number % 3 == 0 and number % 5 == 0:
            output = "FizzBuzz"
            print(output)
        elif number % 3 == 0:
            output = "Fizz"
            print(output)
        elif number % 5 == 0:
            output = "Buzz"
            print(output)
        else:
            print(number)


user_number = int(input())
fizz_buzz(user_number)

# 
# # Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             number="FizzBuzz"
#             print(number)
#         elif number % 3 == 0:
#             number="Fizz"
#             print(number)
#         elif number % 5 == 0:
#             number="Buzz"
#             print(number)
#         else:
#             print(number)
# 
# number=100
# fizz_buzz(number)