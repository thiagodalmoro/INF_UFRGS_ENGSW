from IntruderNotify import *
from SensorConfiguration import *
from tkinter import *

class Application(Frame):

    intruderNotifier:IntruderNotify
    sensorConfig:SensorConfiguration

    def __init__(self, master=None):
        
        self.intruderNotifier = IntruderNotify()
        self.sensorConfig = SensorConfiguration(self.intruderNotifier)

        self.widget = Frame(master)
        self.widget.pack()
        self.toggleIntruder = Checkbutton(self.widget, text="Intruso")
        self.toggleIntruder["command"] = self.simulate_toggleIntruder
        self.toggleIntruder.pack()

    def simulate_toggleIntruder(self):
        self.intruderNotifier.simulate_toggleIntruder()



root = Tk()
root.title("SENSOR DE MOVIMENTO")
root.geometry("400x50")
Application(root)
root.mainloop()
