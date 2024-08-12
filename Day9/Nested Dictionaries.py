travel_log={
    "Country":["Nepal", "India", "Australia", "USA", "Netherland"],
    "City":["Berlin", "Paris", "NewYork", "Pokhara", "Sydney"]
    }
    
print (travel_log["Country"][1])
    
    
nested_list=["a", "b", ["c", "d"]]

print (nested_list[2][0])



my_log={
    "visited_place":{
        "Country":["Nepal", "India", "Australia", "USA", "Netherland"],
        "City":["Berlin", "Pokhara", "NewYork", "Sydney"],
        "total_visited":10
        },
    "unvisited_place":{
        "Country":["Bangladesh", "Pakistan", "China", "North Korea"],
        "City":["Mumbai", "Chennai", "Perth", "Kentucky"],
        "total_visited": 5
        
        }
    }


print(my_log["visited_place"])
print(my_log["visited_place"] ["Country"])
print(my_log["visited_place"] ["City"] [2])
print(my_log["visited_place"]["total_visited"])


print(my_log["unvisited_place"]["City"] [3])
