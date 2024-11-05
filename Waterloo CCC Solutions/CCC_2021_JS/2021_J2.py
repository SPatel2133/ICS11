#Silent Auction
participants = int(input())
highest_bid = 0
highest_bidder = ""
for i in range (participants):
    name = input()
    bid = int(input())
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = name

print(highest_bidder)

