import publishSubscribe
from threading import Thread
from tkinter import *

isBadWeather = False

class MySubscriber(publishSubscribe.Subscriber):
    
    def __init__(self, prefixesList, port, master=None):
        self.socketInit(prefixesList, port)

    def messageReceived(self, message):

        global isBadWeather

        isBadWeather = True
        

class SubscriberThread(Thread):
    subscriber:MySubscriber

    def __init__(self):
        self.subscriber = MySubscriber(["[HumiditySensor]", "[RainSensor]"], 5555)
        Thread.__init__(self)

    def run(self):
        while True:
            self.subscriber.waitForMessage()

class BadWeatherReader(Frame):
    subthread:SubscriberThread
    thisMaster = ""
    label = ""
    
    def __init__(self, master=None):
        
        global currentFrame

        self.thisMaster = master

        self.subthread = SubscriberThread()
        self.subthread.start()

        self.widget = Frame(master)
        self.widget.pack()

        self.label = Label(self.widget)
        self.label["text"] = "Esperando por mau tempo..."
        self.label.pack()
        self.thisMaster.after(1000, self.teste)

    def teste(self):
        global isBadWeather
        if isBadWeather:
            self.label["text"] = "MAU TEMPO DETECTADO"
        self.thisMaster.after(1000, self.teste)