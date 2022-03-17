from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to the SECRET AUCTION PROGRAM")
more_bidders = True

#creating an empty dictionary to keep a record of all the bidders names and their bid
bidder_record = {}

while more_bidders:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidder_record[name] = bid
  ans = input("Are there any more bidders ? Type 'yes' or 'no'.").lower()
  clear()
  print(art.logo)
  if ans == "no":
    more_bidders = False

#finding the highest bid
highest_bid = max(bidder_record,key = bidder_record.get)
print(f"The is winner is {highest_bid} with a bid of ${bidder_record[highest_bid]}.")
print("The auction ends here. THANK YOU!")