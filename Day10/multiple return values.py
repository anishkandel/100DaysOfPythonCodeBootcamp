def format_name(f_name, l_name):
    
    if f_name=="" or l_name=="":
        return "you have not provide the names"
    
    first_name=f_name.title()
    last_name=l_name.title()
    
    return (f"{first_name} {last_name}")


output= format_name(input("what is your first name?"), input("What is your last name?"))

print(output)