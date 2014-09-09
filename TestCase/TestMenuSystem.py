from MenuSystem import MenuManager
from Hardware.SH1106 import SH1106LCD
from Tkinter import *

lcd = SH1106LCD
menuSystem = MenuManager(lcd)

root = Tk()


root.bind("<Up>", MenuManager.upButtonCallback)
root.bind("<Down>", MenuManager.downButtonCallback)
root.bind("<Return>", MenuManager.setButtonCallback)
root.bind("<Shift>", MenuManager.backButtonCallback)

root.mainloop()