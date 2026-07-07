"""
Python Functions

Topics covered:
1. Function inputs, functionality, and output
2. First-class functions
3. Passing functions as arguments (Higher-Order Functions)
4. Nested functions
5. Returning functions
"""

# ==========================================================
# 1. Basic Functions
# ==========================================================


def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Return the difference between two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Return the quotient of two numbers."""
    return n1 / n2


# ==========================================================
# 2. First-Class Functions
# ----------------------------------------------------------
# In Python, functions are first-class objects.
# This means they can:
#   • Be assigned to variables
#   • Be passed as arguments
#   • Be returned from other functions
#   • Be stored in collections (lists, dictionaries, etc.)
# ==========================================================


def calculate(calc_function, n1, n2):
    """Apply the given function to two numbers."""
    return calc_function(n1, n2)


# Example:
# result = calculate(add, 2, 3)
# print(result)      # 5


# ==========================================================
# 3. Nested Functions
# ----------------------------------------------------------
# A function can be defined inside another function.
# The inner function only exists within the scope of
# the outer function.
# ==========================================================

# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
#
# outer_function()


# ==========================================================
# 4. Returning Functions
# ----------------------------------------------------------
# Instead of returning a value, a function can return
# another function.
#
# Notice:
#     return nested_function      ✅ Return the function itself
#     return nested_function()    ❌ Execute the function first
# ==========================================================


def outer_function():

    def nested_function():
        print("I'm inner")

    return nested_function


# Store the returned function in a variable
inner_function = outer_function()

# Execute the returned function
inner_function()
