bids = {}
newbidders = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while newbidders:
    name = input("What is your name?")
    bid = int(input("How much would you like to bid?: $"))
    bids[name] = bid
    newbidders = input("Are there any new more bidders? 'yes' or 'no': \n").lower()
    if newbidders == "no":
        find_highest_bidder(bids)
        newbidders = False
    if newbidders == "yes":
        print("\n" * 100)
