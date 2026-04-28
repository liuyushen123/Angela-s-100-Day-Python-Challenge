import game_data
import random
import art
import os

DATA = game_data.data
another_game = True

def get_players():
    length = len(DATA) - 1
    return random.randint(0, length), random.randint(0, length)

def check_answer(user_guess, num1, num2,score):
    is_a_greater = (DATA[num1]['follower_count'] > DATA[num2]['follower_count'])
    
    if (user_guess.lower() == 'a') and (is_a_greater):
        is_a_greater = True
        score += 1
    elif (user_guess.lower() == 'b') and not (is_a_greater):
        is_a_greater = True
        score += 1
    else:
        is_a_greater = False

    return is_a_greater, score
    



def play_around():
    score = 0
    game_should_continue = True
    while(game_should_continue):
        while (True):
            os.system('clear')
            player1, player2 = get_players()
            if player1 != player2:
                break
        
        print(art.logo)
        if (score):
            print(f"You're right! Current score: {score}")
        print(f"Compare A {DATA[player1]['name']}, {DATA[player1]['description']}, from {DATA[player1]['country']}")
        print(art.vs)
        print(f"Compare B {DATA[player2]["name"]}, {DATA[player2]['description']}, from {DATA[player2]['country']}")
        print(DATA[player1]['follower_count'])
        print(DATA[player2]['follower_count'])
        game_should_continue, score = check_answer(input("Who has more followers? Type \'A\' or \'B\': "),player1, player2, score)
while(another_game):
    play_around()
    user_choice = input("That is unfortunate would you like to play another game?: (y/n)")
    if user_choice.lower() == "n":
        break
    
print("Goodbye")