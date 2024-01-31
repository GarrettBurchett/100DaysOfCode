import os
from art import logo

people_bidding = {}
other_bidders = 'yes'
count = 0

while other_bidders == 'yes':
    if count == 0:
        print(logo)
        print("Welcome to the secret auction program.")
    else:
        os.system('cls')
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    people_bidding[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while other_bidders not in ['yes', 'no']:
        print("Invalid response for if there are other bidders. Accepted responses are 'yes' and 'no'.")
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    count += 1

winner_name = ""
highest_bid = 0
for k, v in people_bidding.items():
    if v > highest_bid:
        winner_name = k
        highest_bid = v
os.system('cls')
print(f"The winner is {winner_name} with a bid of ${highest_bid}")