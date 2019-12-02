import publishSubscribe
from threading import Thread
from tkinter import *
from PIL import ImageTk, Image
import pickle
from cameraFeedReader import CameraFeedReader
from alertModeConfig import AlertModeConfig
from badWeatherReader import BadWeatherReader

class Application:
    def __init__(self, master):
        self.master = master
        self.newWindow = Toplevel(self.master)
        self.cameraFeed = CameraFeedReader(self.newWindow)
        self.newerWindow = Toplevel(self.master)
        self.alertConfig = AlertModeConfig(self.newerWindow)
        self.newererWindow = Toplevel(self.master)
        self.badWeather = BadWeatherReader(self.newererWindow)


root = Tk()
root.title("APLICATIVO")
root.geometry("400x400")
Application(root)
root.mainloop()




