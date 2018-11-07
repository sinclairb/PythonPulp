
class Character:
    """
    A character is any creature, item, or person that can be played or played against
    Each character has a name, level, energy, and powers
    """
    def __init__(self, name="", level=1, powers=[]): 
        """ 
        Contructs a character with default parameters based on level
        """
        # The character's name
        self.name=name
        # The characters level; influences base energy
        self.level=level
        # The amount of energy the character has; influenced by powers and damage from combat
        self.energy=self.calcBaseEnergy()
        # The list of power objects the character possesses; usually between 1 and 5 inclusive
        self.powers=powers
    

    def setName(self, newName):
        """
        Sets the character's name to a new value
        """
        self.level=newName


    def setLevel(self, newLevel):
        """
        Sets the character's level to a new value
        """
        self.level=newLevel


    def calcBaseEnergy(self):
        """
        Based on the character's level, return the energy the character should start with
        """
        base=20
        addition=(5*self.level)
        return base+addition

    def calcEnergy(self):
        """
        Based on the character's base energy, powers, damage sustained, and powers used, return the energy the character should have
        """
        # Calculate the character's base energy
        base=self.calcBaseEnergy
        # 
        return 