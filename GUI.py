import tkinter
import tkinter.ttk
import character
import power
import effect

class MainMenu(tkinter.Frame):
    def __init__(self, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack(fill='both')

        # Button to create a new character, adding a new empty charater tab
        self.newCharacterButton=tkinter.Button(self, text="New Character", command=self.master.addNewCharacter)
        self.newCharacterButton.pack()

        # Fullscreen toggle
        self.fullscreenButton = tkinter.Button(self, text="Toggle Fullscreen", command= lambda: self.master.master.attributes('-fullscreen', (not self.master.master.attributes('-fullscreen'))))
        self.fullscreenButton.pack()

        # Quit button
        self.quitButton = tkinter.Button(self, text="Quit", command=self.master.master.destroy)
        self.quitButton.pack()



class CharacterTabs(tkinter.Frame):
    def __init__(self, *master):
        """
        A Frame that contains tabs for the main menu and loaded characters
        """
        tkinter.Frame.__init__(self,*master)
        self.pack(fill='both')

        # Create the tab menu at the top of the window
        self.tabs=tkinter.ttk.Notebook(self)
        self.tabs.pack(fill='both')
        # Create the main menu tab
        self.mainMenu=MainMenu(self)
        self.tabs.add(self.mainMenu,text="Menu")


    def addNewCharacter(self):
        # Create a new default instance of a character
        newCharacter=character.Character()
        # Create a new CharacterFrame for the new character object
        newCharacterFrame=CharacterFrame(newCharacter, self)
        # Create a new tab to display the information about the new character
        self.tabs.add(newCharacterFrame,text=newCharacter.name)


    def updateName(self, child):
        # Gets the contents of the tab's name entry
        newName=child.characterNameEntry.get()
        # Sets the character's name to the new name
        child.character.setName(newName)
        # Updates the tab's text to match the new name
        self.tabs.tab(child,text=newName+" | "+child.character.epithet+" | "+str(child.character.level))
        # Return true in order to indicate that the update fired
        return True

    
    def updateEpithet(self, child):
        # Gets the contents of the tab's epithet entry
        newEpithet=child.characterEpithetEntry.get()
        # Sets the character's epithet to the new epithet
        child.character.setEpithet(newEpithet)
        # Updates the tab's text to match the new epithet
        self.tabs.tab(child,text=child.character.name+" | "+newEpithet+" | "+str(child.character.level))
        # Return true in order to indicate that the update fired
        return True


    def updateLevel(self, child):
        # Gets the contents of the tab's level entry
        newLevel=child.characterLevelEntry.get()
        # Sets the character's level to the new level
        child.character.setLevel(newLevel)
        # Calculates and updates the character's energy
        child.character.energy=child.character.calcEnergy()
        # Update the energy label to match
        child.characterEnergyDisplay.config(text=child.character.energy)
        # Updates the tab's text to match the new level
        self.tabs.tab(child,text=child.character.name+" | "+child.character.epithet+" | "+str(newLevel))
        # Return true in order to indicate that the update fired
        return True



class CharacterFrame(tkinter.Frame):
    def __init__(self, tiedCharacter, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack(fill='both')

        # The character object that the frame is tied to
        self.character=tiedCharacter

        # A labeled entry to display and edit the character's name
        self.characterNameLabel=tkinter.Label(self,text="Name")
        self.characterNameLabel.pack()
        self.characterNameEntry=tkinter.Entry(self,validate='focus',vcmd=lambda: self.master.updateName(self))
        self.characterNameEntry.pack()
        self.characterNameEntry.delete(0,'end')
        self.characterNameEntry.insert(0,self.character.name)

        # A labeled entry to display and edit the character's epithet
        self.characterEpithetLabel=tkinter.Label(self,text="Epithet")
        self.characterEpithetLabel.pack()
        self.characterEpithetEntry=tkinter.Entry(self,validate='focus',vcmd=lambda: self.master.updateEpithet(self))
        self.characterEpithetEntry.pack()
        self.characterEpithetEntry.delete(0,'end')
        self.characterEpithetEntry.insert(0,self.character.epithet)

        # A labeled entry to display and edit the character's level
        self.characterLevelLabel=tkinter.Label(self,text="Level")
        self.characterLevelLabel.pack()
        self.characterLevelEntry=tkinter.Entry(self,validate='focus',vcmd=lambda: self.master.updateLevel(self))
        self.characterLevelEntry.pack()
        self.characterLevelEntry.delete(0,'end')
        self.characterLevelEntry.insert(0,self.character.level)

        # A label that displays the character's energy
        self.characterEnergyLabel=tkinter.Label(self,text="Energy")
        self.characterEnergyLabel.pack()
        self.characterEnergyDisplay=tkinter.Label(self,text=self.character.energy)
        self.characterEnergyDisplay.pack()

        # A Frame that displays the character's power(s)
        self.powersFrame=PowersFrame(self.character.powers,self)
        self.powersFrame.pack()



class PowersFrame(tkinter.Frame):
    def __init__(self, tiedPowers, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack()

        # The character.powers list that the frame displays
        self.powers=tiedPowers

        # Button that creates another blank power
        self.addPowerButton=tkinter.Button(self, text="Add Power", command=self.addPower)
        self.addPowerButton.pack()

        # Create a PowerFrame to display each power the character has
        for eachPower in self.powers:
            # Create a PowerFrame for each power
            eachPowerFrame=PowerFrame(eachPower,self)
            eachPowerFrame.pack()


    def addPower(self):
        # Create a new default power
        newPower=power.Power()
        # Add the power to the charcter's power list
        self.powers.append(newPower)
        # Create a PowerFrame for the power
        newPowerFrame=PowerFrame(newPower,self)
        newPowerFrame.pack()



class PowerFrame(tkinter.Frame):
    def __init__(self, tiedPower, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack()

        # The power object that the powerframe is tied to
        self.power=tiedPower

        # A labeled entry to display and edit the power's name
        self.powerNameLabel=tkinter.Label(self,text="Power Name")
        self.powerNameLabel.pack()
        self.powerNameEntry=tkinter.Entry(self,validate='focus',vcmd=lambda: self.updateName())
        self.powerNameEntry.pack()
        self.powerNameEntry.delete(0,'end')
        self.powerNameEntry.insert(0,self.power.name)

        # A label that displays the power's potential
        self.powerPotentialLabel=tkinter.Label(self,text="Potential")
        self.powerPotentialLabel.pack()
        self.powerPotentialDisplay=tkinter.Label(self,text=self.power.potential)
        self.powerPotentialDisplay.pack()

        # A label that displays the power's cost
        self.costLabel=tkinter.Label(self,text="Energy Cost")
        self.costLabel.pack()
        self.costDisplay=tkinter.Label(self,text=self.power.cost)
        self.costDisplay.pack()

        # A frame that displays the power's effect(s)
        self.effectsFrame=EffectsFrame(self)
        self.effectsFrame.pack()

        # A labeled textbox to display and edit the power's description
        self.powerDescriptionLabel=tkinter.Label(self,text="Description")
        self.powerDescriptionLabel.pack()
        self.powerDescriptionText=tkinter.Text(self)
        self.powerDescriptionText.bind("<Button-1>",lambda: self.updateDescription())
        self.powerDescriptionText.pack()
        self.powerDescriptionText.delete(1.0,'end')
        self.powerDescriptionText.insert(1.0,self.power.description) 

    
    def updateName(self):
        # Read the contents of the powerNameEntry 
        newName=self.powerNameEntry.get()
        # update the character's power's name to match
        self.power.setName(newName)

    
    def updateDescription(self):
        # Read the contents of the powerDescriptionText 
        newDescription=self.powerDescriptionText.get(1.0,'end')
        # update the character's power's description to match
        self.power.setDescription(newDescription)



class EffectsFrame(tkinter.Frame):
    def __init__(self, tiedEffects, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack()

        # The character.effects list that the frame displays
        self.effects=tiedEffects

        # Displays the label for the effects section
        self.effectsHeader=tkinter.Label(self, text="Effects")
        self.effectsHeader.pack()

        # Button that creates another blank effect
        self.addEffectButton=tkinter.Button(self, text="Add Effect", command=self.addEffect)
        self.addEffectButton.pack()

        # Create a EffectFrame to display each effect the character has
        for eachEffect in self.effects:
            # Create an EffectFrame for each effect
            eachEffectFrame=EffectFrame(eachEffect,self)
            eachEffectFrame.pack()


    def addEffect(self):
        # Create a new default effect
        newEffect=effect.Effect()
        # Add the effect to the charcter's effects list
        self.effects.append(newEffect)
        # Create a EffectFrame for the effect
        newEffectFrame=EffectFrame(newEffect,self)
        newEffectFrame.pack()



class EffectFrame(tkinter.Frame):
    def __init__(self, tiedEffect, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack()

        # The effect object that the powerframe is tied to
        self.effect=tiedEffect

        # A dropdown menu to allow the user to set possible effects
        self.effectDropdown=tkinter.OptionMenu(self, "Effect", *effect.listOfEffects)
        self.effectDropdown.pack()

        # An entry to set and display the points value of the effect
        self.effectPointsEntry=tkinter.Entry(self,validate='focus',vcmd=lambda: self.updatePoints())
        self.effectPointsEntry.pack()

    def updatePoints(self):
        # Read the contents of the powerNameEntry 
        newPoints=self.effectPointsEntry.get()
        # update the effect's points to match
        self.effect.setPoints(newPoints)