"""Barbara Rodríguez López"""
"""GITI9071"""
"""Interator Provides a way to sequentially access the elements of an object"""

def count_to (count):
    """Our iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creatres a tuple such as (1, "eins")
    iterator = zip(range (count), numbers_in_german)

    # Iterate though our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:

        # Returns a 'generator' containing numbers in German
        yield  number

# Let´s test the generator returned by our iterator
for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))