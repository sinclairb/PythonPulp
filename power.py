import effect

class Power:
    """
    Powers are the paramount ways in which characters interact with each other and the environment
    Each power has a name, description, effects, potential, and cost
    """
    def __init__(self, name="", description="", effects=[]):
        # The power's name
        self.name=name
        # A description of what the power does
        self.description=description
        # A two dimensional list of the effect name and its value
        self.effects=effects
        # 
        self.potential=self.calcPotential()
        # 
        self.cost=self.calcCost()


    def setName(self, newName):
        """
        Makes sure the new value is acceptable
        Sets the power's name to a new value
        """
        self.name=str(newName)
    

    def setDescription(self, newDescription):
        """
        Makes sure the new value is acceptable
        Sets the power's description to a new value
        """
        self.description=str(newDescription)


    def calcPotential(self):
        potential=0
        for eachEffect in self.effects:
            # Determines the total cost of a single effect and truncates (rounds cost down)
            eachEffectTotalCost=int(eachEffect.cost*eachEffect.points)
            potential+=eachEffectTotalCost
        return potential


    def setPotential(self, newPotential):
        """
        Makes sure the new value is acceptable
        Sets the power's potential to a new value
        """
        self.potential=int(newPotential)

    
    def calcCost(self):
        return costs[self.potential]


    def setCost(self, newCost):
        """
        Makes sure the new value is acceptable
        Sets the power's cost to a new value
        """
        self.cost=int(newCost)



# A table of potential -to-> cost to use the power
costs={0:0,
             1:1,
             2:1,
             3:1,
             4:2,
             5:2,
             6:2,
             7:3,
             8:3,
             9:3,
             10:5,
             11:5,
             12:5,
             13:8,
             14:8,
             15:8,
             16:10,
             17:10,
             18:10,
             19:12,
             20:12}