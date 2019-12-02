import publishSubscribe
from threading import Thread
from tkinter import *
from PIL import ImageTk, Image
import pickle

currentFrame:Image = Image.open("camera/cameraFrameNoIntruder.jpg")

class MySubscriber(publishSubscribe.Subscriber):
    
    def __init__(self, prefixesList, port, master=None):
        self.socketInit(prefixesList, port)

    def messageReceived(self, message):

        global currentFrame

        data = message[13:]
        dataObj = pickle.loads(data)
        currentFrame = pickle.loads(dataObj["data"])
        

class SubscriberThread(Thread):
    subscriber:MySubscriber

    def __init__(self):
        self.subscriber = MySubscriber(["[CameraFeed]"], 5555)
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
root.title("TESTE CAMERA")
root.geometry("400x400")
Application(root)
root.mainloop()