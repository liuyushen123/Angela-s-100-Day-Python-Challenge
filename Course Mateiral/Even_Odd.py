number_to_check = int(input("What is the number you want to check?: "))

number_to_check = number_to_check % 2

if(number_to_check):
    print("This number is odd")
else:
    print("This number is even")
    