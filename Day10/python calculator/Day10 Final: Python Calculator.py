
import art
def add (n1, n2):
    
  return n1 + n2


#TODO 1: write out other 3 function to subtract multiply and divide

def subtract (n1, n2):
    return n1-n2


def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1/n2
    
    
#TODO 2 : add these 4 functions into  a dictionary as key "+", "*", "-", "/"

calculation={
    
    "+": add,
    "-": subtract,
    "*":multiply,
    "/":divide
    
    }

#TODO 3: use this dictionary to perform multiplication 4** using the dictionary




def calculator():
    print(art.logo)
    should_accumulate=True
    num1=float(input("What's the first number?: "))

    while should_accumulate:
        #TODO 4: ask the input and operation to the user
        
        for symbol in calculation:
            print (symbol)

        operation_symbol=input("Pick an operation: ")

        num2=float(input("What is the next number: "))

        
        answer=calculation[operation_symbol](num1, num2)
        
        print(f" {num1} {operation_symbol} {num2} = {answer}")
        
      


        choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ").lower()
        
        if choice=="y":
           num1=answer
        else:
            should_accumulate=False
            
            print ("\n" * 20)
            
            calculator()
            
calculator()            
        


