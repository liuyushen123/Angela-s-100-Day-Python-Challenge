## Python Decorator Function
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def say_bye():
    print("BYe")


def say_greeting():
    print("How are you?")


original_say_hello = say_hello
say_hello()
original_say_hello()
