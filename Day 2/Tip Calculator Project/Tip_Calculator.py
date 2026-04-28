print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?: "))
total_tip = int(input("How much tip would you like to give?: "))
total_people = int(input("How many people to split the bill?: "))

calculatorResult = (total_bill + total_tip) / total_people
print(f"Each person should pay: {calculatorResult}")