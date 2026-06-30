# When you run the script directly, Python sets the __name__ variable to "__main__"
# This represents the "top-level code execution" scope.
from flask import Flask

print(f"The name of the module is: {__name__}")
app = Flask(__name__)


# This is a standard Python pattern used to ensure code only runs when
# the file is executed directly, not when it is imported as a module.
@app.route("/")
def home():
    return "Hello World!"


if __name__ == "__main__":
    print("This code block only runs if this script is executed directly!")
    # Call your main function here, for example:
    # main()

    app.run(host="0.0.0.0", port=5001, debug=True)
