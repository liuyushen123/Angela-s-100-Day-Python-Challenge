"""The error message means that the string provided to int could not be parsed as an integer"""
""" The program below is crashing because we're are trying to parse a string into integer"""

# age = int(input("How old are you?: "))
# if age > 18:
#     print(f"You can drive at the age {age}")

"""To fix that we can use try expect block to successfully catch this potentially dangerous code"""

while(True):
    try:
        age = int(input("How old are you?: "))
        break
    except ValueError:
        print("That is not the valid input")
if age > 18:
    print(f"You can drive at the age {age}")
