from art import logo
import os
clear = lambda: os.system('cls')



bidders = {}

otherBidders = True

while otherBidders:
    print(logo)
    
    name = input("What is your name: ")
    bid = float(input("What is your bid: $"))
    bidders[name] = bid
    
    others = input("Are there any other bidders? Yes/No\n").lower()
    if others == "no":
        otherBidders = False
    # clear screen
    clear()


max_key = None
max_value = float('-inf')  # Initialize with negative infinity
for key in bidders:
    if bidders[key] > max_value:
        max_key = key
        max_value = bidders[key]


print(f"{max_key} has won the auction with bid {max_value}")  # Returns: 'Jack'
        
    
    
