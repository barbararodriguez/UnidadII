"""Barbara Rodríguez López"""
"""GITI9071"""
"""Compositive Combine objects in tree structures"""
class Component(object):
    def __init__(self, *args, **kwargs):
        pass
    def component_fuction(self):
        pass
class Child(Component): #Inherits from abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of your child item!
        self.name = args[0]

    def component_fuction(self):
        #Print the name of your child item here!
        print("{}".format(self.name))

class Composite(Component): #Inherits from the abstract class, Component
    """"Concrete class maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of the composite object
        self.name = args[0]

        #This is where we keep aor child items
        self.children = []

    def append_child(self, child):
     """Method to add a new child item"""
     self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_fuction(self):

        #Print the name of the composite object
        print("{}".format(self.name))

        #Interate through the child objects and invoke their componet fuction printing theis names
        for i in self.children:
            i.component_fuction()

#Build a compositive submenu 1
sub1 = Composite("submenu1")

#Create a new child sub_sudmenu 11
sub11 = Child("sub_submenu 11")

#Create a new child sub_sudmenu 12
sub12 = Child("sub_submenu 12")
#Add the sub_submenu 11 to wubmenu 1
sub1.append_child(sub11)

#Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)
#Build a top-level composite menu
top = Composite("top_menu")

#Build a submenu 2 that is not a composite
sub2 = Child("submenu2")

#Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)
#Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

#Let's test if our Composite pattern works!
top.component_fuction()

