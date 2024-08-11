def greet(name, location):
    print(f"Hi! My name is {name} and i live in {location}")
    print(f"hello! My name is {name} and i am going to {location}")
    print(f"namaste! sathi, mero name {name} ho ani mero ghar {location} ho")

greet("anish", "nepal")

greet("nepal", "name") #postonal arguments

greet(name="anish", location="Nepal") #keyword Arguments
