import art
import random
import os
import time

logo = art.logo

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def starting_phase(computer_hand, player_hand):
    for i in range(2):
        computer_hand.append(deal_card())
        player_hand.append(deal_card())
    return computer_hand, player_hand

def current_val(deck):
    if (sum(deck) == 21):
        return 0
    if 11 in deck and sum(deck) > 21:
        return sum(deck) - 10
    return sum(deck)

def initlize_game():
    for i in range(2):
        player_hand = [deal_card(),deal_card()]
        computer_hand = [deal_card(),deal_card()]
    return player_hand,computer_hand

def play_round(player_hand, computer_hand,logo):
    time.sleep(0.3)
    os.system('clear')

    print(logo)
    print(f"\tYour cards: {player_hand}, current score: {current_val(player_hand)}")
    print(f"\tComputer's first card: {computer_hand[0]}")
    return


start_game = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")

if start_game == "y":
    player_hand, computer_hand = initlize_game()
    play_round(player_hand,computer_hand,logo)
    while (start_game == 'y'):
        start_game = input("Type \'y\' to get another card, type \'n\' to pass: ")
        if (current_val(player_hand) > 21 or (start_game != 'y')):
            break
        player_hand.append(deal_card())
        play_round(player_hand,computer_hand,logo)
    
    if (current_val(player_hand) > 21):
        print("You're busted. You lose!")
    else:
        while (current_val(computer_hand) < 17):
            number = deal_card()
            computer_hand.append(number)
            print(f"Computer drew {number} final value: {current_val(computer_hand)}")
            time.sleep(0.3)
        if (current_val(computer_hand) > 21):
            print("Computer is busted. You win!")
        elif (current_val(computer_hand) == current_val(player_hand)):
            print("Draw")
        elif ((current_val(computer_hand) > current_val(player_hand))):
            print("Computer won!")
        elif ((current_val(computer_hand) < current_val(player_hand))):
            print("You won!")
        
else:
    print("Goodbye!")






