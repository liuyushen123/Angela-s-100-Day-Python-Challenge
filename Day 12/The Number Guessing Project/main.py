import random
import time
import os

def start():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    mDifficulty = input("Choose a difficulty. Type \'easy\' or \'hard\': ")

    return 5 if (mDifficulty == "hard") else 10

LIVES = start()
GUESS_NUMBER = random.randint(1,100)
RIGHT = False

while(LIVES):
    os.system('clear')
    print(f"You have {LIVES} attempts remaining to guess the number.")
    uGuess = int(input("Make a guess: "))

    if GUESS_NUMBER > uGuess:
        print("Too low.")
        print("Guess again.")
        LIVES -= 1
        time.sleep(2)
    elif GUESS_NUMBER < uGuess:
        print("Too high.")
        print("Guess again.")
        LIVES -= 1
        time.sleep(2)
    elif GUESS_NUMBER == uGuess:
        print("You guessed the right number!")
        LIVES = 0
        RIGHT = True

if not RIGHT:
    print(f"The correct answer was {GUESS_NUMBER}")
