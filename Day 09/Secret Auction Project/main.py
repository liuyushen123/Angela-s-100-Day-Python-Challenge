import os
import random

art = """
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
"""



print(art)
print("Welcome to the secret auction program")
last_person = True
auct_dict = {"dummyBidder": 0}
highest_bidder = "dummyBidder"

while (last_person):
    name = input("What is your name?")
    bid =  int(input("What's your bid?: $"))
    auct_dict[name] = bid
    if auct_dict[highest_bidder] < bid:
        highest_bidder = name

    end = input("Are there any other bidders? Type \'yes\' or \'no\'").lower()
    last_person = True if (end == "yes") else False
    os.system('clear')


print(f"The winner is {highest_bidder} with a bid of ${auct_dict[highest_bidder]}")