
class Character:
    """
    A character is any creature, item, or person that can be played or played against
    Each character has a name, epithet, level, energy, and powers
    """
    def __init__(self, name="Character Name", epithet="", level=1, powers=[]): 
        """ 
        Contructs a character with default parameters based on level
        """
        # The character's name
        self.name=name
        # The character's epithet; a descriptor of who/what they are/their playstyle/class
        self.epithet=epithet
        # The characters level; influences base energy
        self.level=level
        # The amount of energy the character has; influenced by powers and damage from combat
        self.energy=self.calcEnergy()
        # The list of power objects the character possesses; usually between 1 and 5 inclusive
        self.powers=powers
    

    def setName(self, newName):
        """
        Sets the character's name to a new value
        """
        self.name=newName


    def setEpithet(self, newEpithet):
            """
            Sets the character's epithet to a new value
            """
            self.epithet=newEpithet


    def setLevel(self, newLevel):
        """
        Sets the character's level to a new value
        """
        self.level=newLevel


    def calcEnergy(self):
        """
        Based on the character's base energy, powers, damage sustained, and powers used, return the energy the character should have
        """
        base=20
        addition=(5*self.level)
        return base+addition