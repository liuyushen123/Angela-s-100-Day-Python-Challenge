# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_messaage:
    print(f"The key {error_messaage} does not exit.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File is closed")
