"""Barbara Rodríguez López"""
"""GITI9071"""
"""Strategy Permite que un objeto modifique su comportamiento cada vez que cambia su estado interno"""
import types # import the types modules
class Strategy:

    def __init__(self, function = None):
        self.name = "Default Strategy"
 #if a reference to function is provided, replace the execute() method with the given function

    def execute (self): #This gets replaced by another version if another strategy is provided.
        """the defaut method that name of the strategy being used"""
        print("{} is used!".format(self.name))

#Replacement method 1
def strategy_one(self):
    print("{} Is used to execute method 1".format(self.name))

#Replacement method 2
def strategy_two(self):
    print("{} Is used to execute method 2".format(self.name))


#Let's create our default strategy
s0 = Strategy()
#Let's execute our default strategy
s0.execute()


#Let's create the first varition of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
#Let's set its name
s1.name = "Strategy One"
#Let's execute the strategy
s1.execute()

#Let's create the first varition of our default strategy by providing a new behavior
s2 = Strategy(strategy_two)
#Let's set its name
s2.name = "Strategy Two"
#Let's execute the strategy
s2.execute()

