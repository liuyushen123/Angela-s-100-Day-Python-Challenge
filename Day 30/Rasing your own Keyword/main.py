# FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_messaage:
#     print(f"The key {error_messaage} does not exit.")

# else:
#     content = file.read()
#     print(content)

# finally:
#     raise TypeError("This is an error I made up.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height")

bmi = weight / height**2
print(bmi)
