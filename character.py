
# A character is any creature, item, or person that can be played or played against
# Each character has Energy and Powers
# Energy is disctated by powers and 

class Character:
    def __init__(self, level):
        self.level=level
        self.energy=self.calcBaseEnergy(level)
        self.powers=[]
    

    def setLevel(self, newLevel):
        self.level=newLevel


    def calcBaseEnergy(self, level):
        base=20
        addition=(5*level)
        return base+addition
