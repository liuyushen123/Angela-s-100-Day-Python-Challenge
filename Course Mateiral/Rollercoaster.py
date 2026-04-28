height = int(input("What is your height in cm?: "))
age = int(input("What is your age?: "))
isPhoto = input("Do you want to have a photo take?: (y/n)")
ticket_price = 0

if height > 120:
    if (age >= 18):
        ticket_price += 12
    elif (age < 18 and age > 7):
        ticket_price += 7   
    else: 
        ticket_price =+ 5
    
else:
    print("Sorry you have to grwo taller before you can ride.")

if (isPhoto == "y"):
    ticket_price += 3
print(f"Your final bill is {ticket_price}")