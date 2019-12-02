from FireNotify import *
from tkinter import *
import sys

roomNumber = 0

class Application(Frame):

    fireNotifier:FireNotify

    def __init__(self, master=None):
        
        self.fireNotifier = FireNotify()

        self.fireNotifier.setRoomNumber(roomNumber)

        self.widget = Frame(master)
        self.widget.pack()
        self.toggleFire = Checkbutton(self.widget, text="Incendio")
        self.toggleFire["command"] = self.simulate_toggleFire
        self.toggleFire.pack()

    def simulate_toggleFire(self):
        self.fireNotifier.simulate_toggleFire()

if len(sys.argv) > 1:
    roomNumber = sys.argv[1]

root = Tk()
root.title("SENSOR DE FUMAÇA - "+str(roomNumber))
root.geometry("300x50")
Application(root)
root.mainloop()
