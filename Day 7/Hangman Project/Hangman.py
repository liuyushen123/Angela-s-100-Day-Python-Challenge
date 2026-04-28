import random
import os
import time

hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """,
]

os.system("clear")
word_list = [
    "anatomy",
    "biology",
    "medicine",
    "surgery",
    "therapy",
    "diagnosis",
    "symptom",
    "patient",
    "doctor",
    "nurse",
    "hospital",
    "clinic",
    "pharmacy",
    "vaccine",
    "antibody",
    "infection",
    "virus",
    "bacteria",
    "immunity",
    "disease",
    "fracture",
    "injury",
    "trauma",
    "tumor",
    "cancer",
    "lesion",
    "biopsy",
    "anemia",
    "diabetes",
    "asthma",
    "arthritis",
    "allergy",
    "epidemic",
    "pandemic",
    "cardiology",
    "neurology",
    "dermatology",
    "psychiatry",
    "radiology",
    "oncology",
    "pediatrics",
    "pathology",
    "orthopedics",
    "hematology",
    "imaging",
    "ultrasound",
    "xray",
    "scanner",
    "microscope",
    "stethoscope",
    "syringe",
    "bandage",
    "ointment",
    "capsule",
    "tablet",
    "dosage",
    "prescription",
    "treatment",
    "recovery",
    "rehabilitation",
    "monitoring",
    "ventilator",
    "oxygen",
    "respiration",
    "circulation",
    "heartbeat",
    "pressure",
    "cholesterol",
    "metabolism",
    "digestion",
    "nutrition",
    "hydration",
    "enzyme",
    "hormone",
    "insulin",
    "adrenaline",
    "neuron",
    "muscle",
    "tissue",
    "organ",
    "liver",
    "kidney",
    "stomach",
    "intestine",
    "pancreas",
    "thyroid",
    "immune",
    "skeletal",
    "vascular",
]

wrong_guess = []

randomWord = random.choice(word_list)

life = 7
print(hangman_stages[0])
print(f"*********************{life}/7 LIVES*********************")

display = ""

for i in range(len(randomWord)):
    display += "_"

place_holder = []
game_over = True

while game_over:
    print(f"What is your guess?: {display}")
    print(f"So far you've guessed: {wrong_guess}")
    uGuess = input("Guess a letter: ").lower()
    display = ""

    while len(uGuess) > 1:
        print("Too many letters!")
        uGuess = input("Please re-enter your guess?: ").lower()
    while uGuess in wrong_guess:
        print("That letter is already guessed")
        uGuess = input("Guess a letter: ").lower()

    for i in randomWord:
        if i == uGuess:
            display += uGuess
            place_holder.append(uGuess)
        elif i in place_holder:
            display += i
        else:
            display += "_"
    if uGuess not in randomWord:
        life -= 1
        wrong_guess.append(uGuess)
        print(f"You guessed {uGuess}, That is not the right word. You lost a life")
        input("Type anything to continue")
        if life == 0:
            print(f"The correct word was {randomWord}")
            input("Press Enter to continue")
            game_over = False

    if "_" not in display:
        print("Congrats! You guessed the right word")
        break
    os.system("clear")
    print(hangman_stages[-life])
    print(f"*********************{life}/7 LIVES*********************")
