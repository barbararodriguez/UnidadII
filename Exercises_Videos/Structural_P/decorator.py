"""Barbara Rodríguez López"""
"""GITI9071"""
"""Decorator dynamically add new responsibilities to an object"""

from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # this makes the decorator transparent in terms of its name and docstring

    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being the decorated
        ret = function()

        # Add a new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# Apply decorator here!
@make_blink
def hello_world():
    """ Original function"""
    return "Hello World!"

    # check the result of decorating
    print(hello_world())
    # check if the function name is still same name of the function being decorated
    print(hello_world.__name__)
    # check if the docstring is still the same as that of the function being decorated
    print(hello_world.__doc__)
