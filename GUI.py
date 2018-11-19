import tkinter
import tkinter.ttk
import character
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
        child.character.characterEnergyDisplay.config(text=child.character.energy)
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

        # A test button to print a value of the character
        #self.test=tkinter.Button(self, text="Print Name", command=lambda: print(self.character.name))
        #self.test.pack()



class EffectsFrame(tkinter.Frame):
    def __init__(self, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack()

        # Displays the label for the effects section
        # **Will eventually be able to collapse and expand the list of effects
        self.effectsHeader=tkinter.Label(self, text="Effects")
        self.effectsHeader.pack()

        # Five dropdown menus to allow the user to set possible effects
        self.effect1=tkinter.OptionMenu(self, "Effect1", *effect.listOfEffects)
        self.effect1.pack()
        self.effect2=tkinter.OptionMenu(self, "Effect2", *effect.listOfEffects)
        self.effect2.pack()
        self.effect3=tkinter.OptionMenu(self, "Effect3", *effect.listOfEffects)
        self.effect3.pack()
        self.effect4=tkinter.OptionMenu(self, "Effect4", *effect.listOfEffects)
        self.effect4.pack()
        self.effect5=tkinter.OptionMenu(self, "Effect5", *effect.listOfEffects)
        self.effect5.pack()