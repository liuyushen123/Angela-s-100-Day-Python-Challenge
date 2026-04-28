import art
import os

logo = art.logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square(n1, n2):
    return n1 ** n2


calculator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": square,
    }




result = -1



while True:
    os.system('clear')
    print(logo)
    number1 = int(input("What is your first number: "))
    should_continue = True
    while (should_continue):
        for i in calculator_dict:
            print(i)
        operation = input("Pick an operations: ")
        number2 = float(input("What is your next number?: "))
        result = calculator_dict[operation](number1, number2)

        print(f"{float(number1)} {operation} {float(number2)} = {float(result)}")
        should_continue = input(f"Type \'y\' to continue to calculationg with {float(result)} or type \'n\' to start a new calculation: ")

        if should_continue == 'y':
            should_continue = True
            number1 = result
        else:
            should_continue = False
