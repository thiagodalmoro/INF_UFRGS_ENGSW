import publishSubscribe
from threading import Thread
from tkinter import *
from PIL import ImageTk, Image
import pickle

normalControlScreen = Image.open("normalControlScreen.jpg")
currentFrame:Image = normalControlScreen

class ControlScreenSubscriber(publishSubscribe.Subscriber):
    
    def __init__(self, prefixesList, port, master=None):
        self.socketInit(prefixesList, port)

    def messageReceived(self, message):

        global currentFrame
        messageArray = message.split()
        roomNumber = str(messageArray[1])[2:3]
        currentFrame = Image.open('fireInRoom'+roomNumber+'.jpg')
        

class SubscriberThread(Thread):
    subscriber:ControlScreenSubscriber

    def __init__(self):
        self.subscriber = ControlScreenSubscriber(["[SmokeSensor]", "[TemperatureSensor]"], 5555)
        Thread.__init__(self)

    def run(self):
        while True:
            self.subscriber.waitForMessage()

class Application(Frame):
    subthread:SubscriberThread
    thisMaster = ""
    
    def __init__(self, master=None):
        
        global currentFrame

        self.thisMaster = master

        self.subthread = SubscriberThread()
        self.subthread.start()

        self.widget = Frame(master)
        self.widget.pack()

        frame = ImageTk.PhotoImage(currentFrame)

        self.panel = Label(root, image=frame)
        self.panel.configure(image=frame)
        self.panel.image = frame
        self.panel.pack(side="bottom", fill="both", expand="yes")

        master.after(1000, self.teste)

    def teste(self):

        global currentFrame

        frame = ImageTk.PhotoImage(currentFrame)

        self.panel.configure(image=frame)
        self.panel.image = frame
        self.thisMaster.after(1000, self.teste)

root = Tk()
root.title("TELA DE CONTROLE")
root.geometry("500x500")
Application(root)
root.mainloop()