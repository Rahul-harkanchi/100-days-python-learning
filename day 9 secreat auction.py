logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
from replit import clear

#HINT: You can call clear() to clear the output in the console.
print(logo)
bids={}

bidding_over=False
while not bidding_over:
    name=str(input("What is your Name?: "))
    bid=int(input("What is your bid?: $"))
    bids[name]=bid
    right_choice=False
    while not right_choice:
        moreBidders=str(input("Are there any other bidders? Type 'yes' or 'no'"))
        moreBidders.lower()
        if moreBidders=="no":
            bidding_over=True
            right_choice=True
        elif moreBidders=="yes":
            clear()
            right_choice=True
        else:
            print("not entered  a right choice")
        
print(bids)
win_score=0
winner=None
for key in bids:
    if bids[key]>win_score:
        winner=key
        win_score=bids[key]
print(f"The winner is {winner} with a bid of ${win_score}")
