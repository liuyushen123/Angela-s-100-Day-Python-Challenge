print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
choosen_pizza_size = ""
total_bill = 0
isPepperoni = False
isExtraCheese = False

if (size == "L"):
    total_bill += 25
    choosen_pizza_size = "Large Pizza"
elif (size == "M"):
    total_bill += 20
    choosen_pizza_size = "Medium Pizza"
elif (size == "S"):
    total_bill += 15
    choosen_pizza_size = "Small Pizza"
else:
    print("Error not a valid input 404")
    print("Ending program")
if (pepperoni == "Y"):
    if (choosen_pizza_size == "Large Pizza" or choosen_pizza_size == "Medium Pizza"):
        total_bill += 3
    elif(choosen_pizza_size == "Small Pizza"):
        total_bill += 2
    else:
        print("Status 404 something went wrong on our end")
elif (pepperoni == "N"):
    print("No pepperoni")
else:
    print("Status 404 invalid input")

if (extra_cheese == "Y"):
    total_bill += 1
elif (extra_cheese == "N"):
    print("No extra cheese added")
else:
    print("404")

print(f"Your total bill is {total_bill}.")