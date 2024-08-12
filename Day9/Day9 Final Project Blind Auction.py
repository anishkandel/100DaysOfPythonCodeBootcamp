# TODO 1: Ask the name input & bid 
#TODO 4: Compare the dictionary which user has highest bid and print out
def find_highest_bid(bid_dictionary):
    highest_bid=0
    winner=""
    for bidder in bid_dictionary:
        bid_amount=bid_dictionary[bidder]
#         print(bid_amount)
        if bid_amount> highest_bid:
            highest_bid=bid_amount
#             print(highest_bid)
            winner=bidder
    print(f" The bid winner is {winner} with the highest bid of {highest_bid}")        


# TODO 2: Save the input in dictionary into key and values
bid={}


#TODO 3: Ask again if there others users to bid, if yes start from TODO 1, if no, show the highest bid
continue_bidding=True
while continue_bidding:
    name=input("What is your name?")
    price=int(input("What is your bid price? $"))
    bid[name]=price
    print (bid) #{'anish': 200, 'kandel': 200, 'shree': 300}

    should_continue=input("Any users to bid more. 'yes' and 'no'").lower()
    if should_continue=='no':
        continue_bidding=False
        find_highest_bid(bid)
    elif should_continue=='yes':
        print("\n"*20)


    

           
       
        
    