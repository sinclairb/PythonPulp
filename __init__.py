
import GUI
import character
import power
import effect
import tkinter


# The window serves as a driver because it is an event listener
# Create the window that the program will run in
window=tkinter.Tk()
# What the program will display as
window.title("Pulp")
# Makes the window fullscreen if set to true
window.attributes('-fullscreen', False)
# Displays the below objects

effectsFrame=tkinter.Frame(window)

window.mainloop()