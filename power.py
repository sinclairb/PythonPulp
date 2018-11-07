import effect

class Power:
    def __init__(self, name="", description="", effects=[]):
        self.name=name
        self.description=description
        self.effects=effects
        self.potential=self.calcPotential()
        self.energyCost=self.calcEnergyCost()


    def calcPotential(self):
        potential=0
        for eachEffect in self.effects:
            # Determines the total cost of a single effect and truncates (rounds cost down)
            eachEffectTotalCost=int(eachEffect.cost*eachEffect.points)
            potential+=eachEffectTotalCost
        return potential

    
    def calcEnergyCost(self):
        return energyCosts[self.potential]


    def addEffect(self, effectName, points=0):
        effect.effectNameToObject(effectName)
        self.effects.append()


    def removeEffect(self, effectName):
        for eachEffect in self.effects:
            if effectName==eachEffect.__class__.__name__:
                self.effects.remove(eachEffect)


# A table of potential -to-> cost to use the power
energyCosts={0:0,
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