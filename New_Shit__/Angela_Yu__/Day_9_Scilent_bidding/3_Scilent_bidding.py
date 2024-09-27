from os import system

BID_RECORD = {}

system("cls")
while 1:
    name_of_bidder = input("What is your name? ")
    amount_of_bid = int(input("What is your bidding amount? $"))
    BID_RECORD.update({amount_of_bid: name_of_bidder})
    winner_bid = max(BID_RECORD.keys())
    winner_name = BID_RECORD[winner_bid]
    next = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if next == "yes" or next == "y" or next == "Y":
        system("clear")
        continue
    elif next == "no" or next == "n" or next == "N":
        system("clear")
        print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
        break
