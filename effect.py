
def effectNameToObject(name):
    # Create a new instance of the effect with a classname of name
    instance = eval(name)()
    return instance

class Effect:
    def __init__(self, cost=0, description="", points=0):
        self.cost=cost
        self.descrption=description
        self.points=points


    def addPoints(self, numOfPoints):
        self.points+=numOfPoints

    
    def setPoints(self, newPoints):
        self.points=newPoints


class Damage(Effect):
    def __init__(self):
        cost=0.6
        descrption="Decreases a target's energy"
        Effect.__init__(self, cost, descrption)


class Healing(Effect):
    def __init__(self):
        cost=1.33
        descrption="Increases a target's energy."
        Effect.__init__(self, cost, descrption)


class AdditionalTarget(Effect):
    def __init__(self):
        cost=2.5
        descrption="Allows the power to affect more targets\nAt 10 additional targets, the power affects an unlimited number"
        Effect.__init__(self, cost, descrption)


class Multiplication(Effect):
    def __init__(self):
        cost=3.5
        descrption="Multiplies the effects of another power used by a target\nDoes not affect other multiplication effects"
        Effect.__init__(self, cost, descrption)


class Negation(Effect):
    def __init__(self):
        cost=0.75
        descrption="Decreases the effects of a power"
        Effect.__init__(self, cost, descrption)


class Persistence(Effect):
    def __init__(self):
        cost=2.5
        descrption="Applies the effects of a power over multiple turns"
        Effect.__init__(self, cost, descrption)


class Paralysis(Effect):
    def __init__(self):
        cost=5
        descrption="Interferes with a target's powers"
        Effect.__init__(self, cost, descrption)


class Confusion(Effect):
    def __init__(self):
        cost=3
        descrption="Interferes with a target's effects or targeting"
        Effect.__init__(self, cost, descrption)


listOfEffects={"Damage",
               "Healing",
               "Additional Target",
               "Multiplication",
               "Negation",
               "Persistence",
               "Paralysis",
               "Confusion"}