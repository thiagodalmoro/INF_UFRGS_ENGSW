from tkinter import *
from threading import Thread
import publishSubscribe

isLocked = False

class SmartlockSubscriber(publishSubscribe.Subscriber):
    
    def __init__(self, prefixesList, port, master=None):
        self.socketInit(prefixesList, port)

    def messageReceived(self, message):
        global isLocked
        messageArray = message.split()

        if(messageArray[0] == "[Camera]" or messageArray[0] == "[MovementSensor]"):
            isLocked = True
        else:
            lockState = str(messageArray[1])[2:3]
            if(lockState == "0"):
                isLocked = False
            else:
                isLocked = True
        

class SubscriberThread(Thread):
    subscriber:SmartlockSubscriber

    def __init__(self):
        self.subscriber = SmartlockSubscriber(["[SmartlockConfig]", "[Camera]", "[MovementSensor]"], 5555)
        Thread.__init__(self)

    def run(self):
        while True:
            self.subscriber.waitForMessage()

class Application(Frame):

    subThread:SubscriberThread
    thisMaster = ""
    msg = ""

    def __init__(self, master=None):
        
        self.subThread = SubscriberThread()
        self.subThread.start()
        self.thisMaster = master

        self.widget = Frame(master)
        self.widget.pack()
        self.msg = Label(self.widget, text="Smartlock destrancada")
        self.msg.pack ()

        master.after(1000, self.updateLockStateText)

    def updateLockStateText(self):
        global isLocked
        if(isLocked):
            self.msg["text"]="Smartlock trancada"
        else:
             self.msg["text"]="Smartlock destrancada"

        self.thisMaster.after(1000, self.updateLockStateText)

if len(sys.argv) > 1:
    roomNumber = sys.argv[1]

root = Tk()
root.title("SMARTLOCK")
root.geometry("300x50")
Application(root)
root.mainloop()
