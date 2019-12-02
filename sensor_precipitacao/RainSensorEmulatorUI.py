from BadWeatherNotify import *
from tkinter import *

class Application(Frame):

    badWeatherNotifier:BadWeatherNotify

    def __init__(self, master=None):
        
        self.badWeatherNotifier = BadWeatherNotify()

        self.widget = Frame(master)
        self.widget.pack()
        self.toggleBadWeather = Checkbutton(self.widget, text="Mau tempo")
        self.toggleBadWeather["command"] = self.simulate_toggleBadWeather
        self.toggleBadWeather.pack()

    def simulate_toggleBadWeather(self):
        self.badWeatherNotifier.simulate_toggleBadWeather()



root = Tk()
root.title("SENSOR DE PRECIPITAÇÃO")
root.geometry("400x50")
Application(root)
root.mainloop()
