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
        newCharacterFrame=CharacterFrame(newCharacter)
        # Create a new tab to display the information about the new character
        self.tabs.add(newCharacterFrame,text=newCharacter.name)



class CharacterFrame(tkinter.Frame):
    def __init__(self, tiedCharacter, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack(fill='both')

        # The character object that the frame is tied to
        self.character=tiedCharacter

        # An entry to display and edit the character's name
        self.characterNameEntry=tkinter.Entry(self)
        self.characterNameEntry.pack()
        self.characterNameEntry.delete(0,'end')
        self.characterNameEntry.insert(0,self.character.name)



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



def update():
    pass