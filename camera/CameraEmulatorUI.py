from IntruderNotify import *
from CameraConfiguration import *
from CameraFeed import *
from tkinter import *
from PIL import ImageTk, Image

class Application(Frame):

    intruderNotifier:IntruderNotify
    cameraConfig:CameraConfiguration
    cameraFeed:CameraFeed
    currentCameraFrame = ""

    def __init__(self, master=None):
        
        self.intruderNotifier = IntruderNotify()
        self.cameraConfig = CameraConfiguration(self.intruderNotifier.intruderChecker)
        self.cameraFeed = CameraFeed(self.intruderNotifier.intruderChecker.cameraData)
        self.currentCameraFrame = ImageTk.PhotoImage(Image.open("cameraFrameNoIntruder.jpg"))

        self.widget = Frame(master)
        self.widget.pack()
        self.toggleIntruder = Checkbutton(self.widget, text="Intruso")
        self.toggleIntruder["command"] = self.simulate_toggleIntruder
        self.toggleIntruder.pack()


        self.panel = Label(root, image=self.currentCameraFrame)
        self.panel.pack(side="bottom", fill="both", expand="yes")

    def simulate_toggleIntruder(self):
        self.intruderNotifier.simulate_toggleIntruder()

        self.currentCameraFrame = ImageTk.PhotoImage(self.cameraFeed.getCurrentFrame())

        self.panel.configure(image=self.currentCameraFrame)
        self.panel.image = self.currentCameraFrame



root = Tk()
root.title("CAMERA")
root.geometry("400x400")
Application(root)
root.mainloop()
