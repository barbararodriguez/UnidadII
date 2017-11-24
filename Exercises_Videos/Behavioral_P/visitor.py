"""Barbara Rodríguez López"""
"""GITI9071"""
"""Visitor Representa una operación sobre los elementos de una estructura"""

class House(object): # the class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        # Triggers the visiting operation!

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist) # Note that we now have a reference to the HVAC specialist object in the house object!

    def work_on_electricity(self, electricion):
        # Note that we now have a reference to the electrician object in the house object!

     def __str__(self):
        """Simply return the class name when nthe House object is printed"""
        return self.__class__.__name__

class Visitor(object):
    """"Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor): # Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""
    def vist (self, house):
        house.work_on_hvac(self) # Note that the visitor now has a reference to the house object

class Electrician(Visitor): # Inherits from the parent class, Visitor
    """concrete visitor: electrician"""
    def visit (self, house):
           house.work_on_electricity # Note that the visitor now has a reference to the house object

# Create an HVAC specialist
hv = HvacSpecialist()

# Create an electrician
e = Electrician()

# Create a house
home = House()

# Let the house accept the HVAC specialist and work om the by invoking the visit() method
home.accept(hv)

# Let the house the electrician and work on the house by inovoking the viait() method
home.accept(e)

