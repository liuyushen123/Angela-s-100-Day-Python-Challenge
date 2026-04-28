number_to_check = int(input("What is the number you want to check? "))

#If a number is divisible by two it is even!

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

# This will print number check with its last digit chopped off
## // Will trauncate the decimals
print(number_to_check // 10)

#In pattern 100 will chop off the last two

# This will only keep the last digit and so on

print(number_to_check % 10)