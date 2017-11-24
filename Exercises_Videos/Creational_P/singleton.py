"""Barbara Rodríguez López"""
"""GITI9071"""
"""Singleton Ensures that a certain class is instantiated"""
class Borg():
    """Borg class making class attributes global"""
    _shared_state = {}
    # Attribute dicctionary

    def __init__(self):
        self._dict_ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Brog class
    """This class now shares all its attributes among its various instances"""
    #this essenstially make the singleton objects an object-oribted global variable
    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __set__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


# let's Create a singleton object and add our first acronym
x = Singleton(HTTP = "Hyper Text Tansfer Protocl")
# print the object
print(x)

# Let's Create anothes singleton object and if it refers to the some attribute dictionary
y = Singleton(SNMP="Simple Network Management Protocol")
# print the object
print(y)
