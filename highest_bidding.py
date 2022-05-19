from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
#flag == yes
winner = ""
bidding = {}
biggest = 0
while True:
  clear()
  print(logo)
  print("Welcome to the secret auction program. ")
  username = str(input("What is your name? "))
  bid = int(input("What's your bid? "))
  flag = str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))
  bidding[username] = bid
  if flag == "no":
    for eachbid in bidding:
      user = list(bidding[0])
      bids = bidding[eachbid]
      if biggest < bids:
        biggest = bids
    print(f"Winner is {user}, {biggest}")
    break
