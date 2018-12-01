from collections import OrderedDict

class Effect:
    def __init__(self, name="", cost=0, points=0):
        self.name=name
        self.cost=cost
        self.points=points


    def setName(self, newName):
        """
        Makes sure the new value is acceptable
        Sets the effect's name to a new value
        """
        self.name=str(newName)

    
    def setPoints(self, newPoints):
        """
        Makes sure the new value is acceptable
        Sets the effect's points to a new value
        """
        self.points=int(newPoints)

    
    def setCost(self, newCost):
        """
        Makes sure the new value is acceptable
        Sets the effect's points to a new value
        """
        self.cost=float(newCost)



# A disctionary of the effects' names and their respective costs
listOfEffects=OrderedDict({"Damage":0.6,
               "Healing":1.33,
               "Additional Target":2.5,
               "Multiplication":3.5,
               "Negation":0.75,
               "Persistence":2.5,
               "Paralysis":6,
               "Confusion":6})