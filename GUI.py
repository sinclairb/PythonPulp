import tkinter
import tkinter.ttk
import effect

class MainMenu(tkinter.Frame):
    def __init__(self, *master):
        tkinter.Frame.__init__(self,*master)
        self.pack(fill='both')

        # Button to create a new character
        newCharacterButton=tkinter.Button(self, text="New")
        newCharacterButton.pack()

class CharacterTabs(tkinter.Frame):
    def __init__(self, *master):
        """
        A Frame that contains tabs for the main menu and loaded characters
        """
        tkinter.Frame.__init__(self,*master)
        self.pack(fill='both')

        # A list of all character objects that are loaded
        self.listOfLoadedCharacters=[]

        # The tab menu at the top of the window
        self.tabs=tkinter.ttk.Notebook(self)
        self.tabs.pack(fill='both')
        # The main menu tab
        self.mainMenu=MainMenu(self)
        self.tabs.add(self.mainMenu,text="Menu")

class CharacterFrame(tkinter.Frame):
    """
    A swappable character frame is identical to a frame, but has the switchTo function, 
    allowing it to be destroyed and replaced by a new frame.
    """
    def __init__(self,*master):
        tkinter.Frame.__init__(self,*master)
        self.pack()

    def switchTo(self, newFrame):
        """
        Creates a new frame of the newFrame parameter type, and destroys itself
        """
        newFrame()
        self.destroy()

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