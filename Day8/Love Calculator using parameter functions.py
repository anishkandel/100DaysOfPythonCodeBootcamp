
def calculate_love_score(name1, name2):
  combined_names=(name1+name2).lower()
#   print(combined_names)
  
  t=combined_names.count("t")
  r=combined_names.count("r")
  u=combined_names.count("u")
  e=combined_names.count("e")
  
  first_digit=str(t+r+u+e)
  
  
  l=combined_names.count("l")
  o=combined_names.count("o")
  v=combined_names.count("v")
  e=combined_names.count("e")
  
  second_digit=str(l+o+v+e)
  
  final_score=(first_digit + second_digit)
  print(final_score)
  
calculate_love_score(name1="Kanye West", name2="Kim Kardashian")