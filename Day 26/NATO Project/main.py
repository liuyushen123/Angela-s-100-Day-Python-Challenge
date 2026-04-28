import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
PATH = "/Users/liuyuchen/Downloads/General Coding/Udemy Course/AngelaYu_100DaysPython/Day 26/NATO Project/nato_phonetic_alphabet.csv"
myList = pandas.DataFrame(pandas.read_csv(PATH))

myDict = {row.letter: row.code for (index, row) in myList.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
userName = input("What is your name?: ").lower()
outputList = []
for i in userName:
    outputList.append(myDict[i.upper()])

print(outputList)
